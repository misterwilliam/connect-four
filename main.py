import os
import pickle

from game import Game
from self_play import SelfPlay

import game_stats_tree

pickle_filename = "game_stats.pickle"
if os.path.isfile(pickle_filename):
  with open(pickle_filename, "rb") as pickle_file:
    game_stats = pickle.load(pickle_file)
else:
  game_stats = game_stats_tree.Node()

game_stats_tree.print_stats(game_stats)

g = Game()

runtime = SelfPlay(g, game_stats)
runtime.play()

game_stats_tree.update_game_stats(game_stats, runtime.log, g.winner)

with open(pickle_filename, "wb") as pickle_file:
  pickle.dump(game_stats, pickle_file)