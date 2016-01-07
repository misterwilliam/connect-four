import argparse
import os
import pickle

from game import Game, DiscState
from move_chooser import MoveChooser, BestKnownMoveChooser
from self_play import SelfPlay
from textual_runtime import TextualRuntime

import game_stats_tree

# Setup command line arguments
parser = argparse.ArgumentParser(description="Train and play against a Connect 4 AI.")
command_parser = parser.add_subparsers(dest="command")

# Configure train command
train_parser = command_parser.add_parser("train", help="Train models")
train_parser.add_argument("models", nargs="+", help="List of models to train")
train_parser.add_argument("--iters", nargs=1, type=int, default=1000,
  help="Number of iterations used to train each model.")

# Configure compare command
compare_parser = command_parser.add_parser("compare",
  help="Compare performance of models")
compare_parser.add_argument("models", nargs=2, help="Models to compare")
compare_parser.add_argument("--iters", nargs=1, type=int, default=100,
  help="Number of play throughs used to compare models.")

# Configure play command
play_parser = command_parser.add_parser("play", help="Play against a model")
play_parser.add_argument("model", nargs=1, help="Models to play against")



def train(models, num_iters):
  for model_path in models:
    if os.path.isfile(model_path):
      with open(model_path, "rb") as pickle_file:
        game_stats = pickle.load(pickle_file)
    else:
      game_stats = game_stats_tree.Node()

    move_chooser = BestKnownMoveChooser(game_stats, exploitation_rate=0.7)
    game_stats_tree.print_stats(game_stats)

    runtime = SelfPlay(move_chooser)

    wins = 0
    for i in range(num_iters):
      g = Game()
      runtime.play(g)
      game_stats_tree.update_game_stats(game_stats, runtime.log, g.winner)
      if g.winner is DiscState.red:
        wins += 1
      if i % 500 == 0 and i > 0:
        print("Runs: %i 1st player win %%: %f" % (i, wins / i))
      if i % 100000 == 0 and i > 0:
        with open(model_path, "wb") as pickle_file:
          pickle.dump(game_stats, pickle_file)
    print("Runs: %i" % num_iters)

    with open(model_path, "wb") as pickle_file:
      pickle.dump(game_stats, pickle_file)

def main():
  args = parser.parse_args()
  if args.command == "train":
    train(args.models, args.iters)





# PLAY = True
# if PLAY:
#   g = Game()
#   runtime = TextualRuntime(g, BestKnownMoveChooser(game_stats, exploitation_rate=1.0,
#     verbose=True))
#   runtime.start()

if __name__ == "__main__":
  main()