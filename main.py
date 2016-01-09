import argparse
import cProfile
import os
import pickle
import pstats

from game import Game, DiscState
from best_known_move_chooser import BestKnownMoveChooser
from connect_four_heuristics import heuristic_move
from uniform_move_chooser import UniformMoveChooser

from compare_runtime import CompareRuntime
from textual_runtime import TextualRuntime
from train_runtime import TrainRuntime

import game_stats_tree

# Setup command line arguments
parser = argparse.ArgumentParser(description="Train and play against a Connect 4 AI.")
command_parser = parser.add_subparsers(dest="command")

# Configure train command
train_parser = command_parser.add_parser("train", help="Train models")
train_parser.add_argument("models", nargs="+", help="List of models to train")
train_parser.add_argument("--iters", type=int, default=100000,
  help="Number of iterations used to train each model.")
train_parser.add_argument("--exploitation_rate", type=float, default=0.65,
  help="Number of iterations used to train each model.")
train_parser.add_argument("--method", choices=["best", "uniform"], default="best")
train_parser.add_argument("--profile", action="store_true", default=False)

# Configure compare command
compare_parser = command_parser.add_parser("compare",
  help="Compare performance of models")
compare_parser.add_argument("models", nargs=2, help="Models to compare")
compare_parser.add_argument("--iters", type=int, default=500,
  help="Number of play throughs used to compare models.")

# Configure play command
play_parser = command_parser.add_parser("play", help="Play against a model")
play_parser.add_argument("model", nargs=1, help="Models to play against")

def get_model(path_to_model):
  if os.path.isfile(path_to_model):
    with open(path_to_model, "rb") as pickle_file:
      game_stats = pickle.load(pickle_file)
  else:
    game_stats = game_stats_tree.Node()
  return game_stats

def train(models, num_iters, exploitation_rate, method, profile):
  if profile:
    pr = cProfile.Profile()
    pr.enable()

  for model_path in models:
    game_stats = get_model(model_path)

    if method == "best":
      move_chooser = BestKnownMoveChooser(game_stats, exploitation_rate,
        heuristic_move_chooser=heuristic_move)
    elif method == "uniform":
      move_chooser = UniformMoveChooser(game_stats, exploitation_rate)
    game_stats_tree.print_stats(game_stats)

    runtime = TrainRuntime(Game(), move_chooser, game_stats, model_path)
    runtime.start(num_iters)

  if profile:
    ps = pstats.Stats(pr).sort_stats("cumtime")
    ps.print_stats()

def compare(model_a, model_b, num_iters):
  move_chooser_a = BestKnownMoveChooser(get_model(model_a))
  move_chooser_b = BestKnownMoveChooser(get_model(model_b))
  runtime = CompareRuntime(Game(), move_chooser_a, move_chooser_b, num_iters)
  a_wins, b_wins = runtime.start()
  print("Win Rates (iters: %i)" % num_iters)
  print("%s: %.2f%%" % (model_a, a_wins * 100 / num_iters))
  print("%s: %.2f%%" % (model_b, b_wins * 100 / num_iters))

def play(path_to_model):
  model = get_model(path_to_model)
  runtime = TextualRuntime(Game(),
                           BestKnownMoveChooser(model,
                                                heuristic_move_chooser=heuristic_move,
                                                verbose=True))
  runtime.start()

def main():
  args = parser.parse_args()
  if args.command == "train":
    train(args.models, args.iters, args.exploitation_rate, args.method, args.profile)
  elif args.command == "play":
    play(args.model[0])
  elif args.command == "compare":
    compare(args.models[0], args.models[1], args.iters)

if __name__ == "__main__":
  main()