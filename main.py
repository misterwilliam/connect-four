import os
import pickle

from game import Game, DiscState
from self_play import SelfPlay

import game_stats_tree

pickle_filename = "game_stats.pickle"
if os.path.isfile(pickle_filename):
  with open(pickle_filename, "rb") as pickle_file:
    game_stats = pickle.load(pickle_file)
else:
  game_stats = game_stats_tree.Node()

game_stats_tree.print_stats(game_stats)

runtime = SelfPlay(game_stats)

wins = 0
num_rounds = 10000
for i in range(num_rounds):
  g = Game()
  runtime.play(g)
  game_stats_tree.update_game_stats(game_stats, runtime.log, g.winner)
  if g.winner is DiscState.red:
    wins += 1
  if i % 100 == 0 and i > 0:
    print("Wins: %f" % (wins / i))

print("Wins: %f" % (wins / num_rounds))

with open(pickle_filename, "wb") as pickle_file:
  pickle.dump(game_stats, pickle_file)