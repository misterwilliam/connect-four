from game import Game
from self_play import SelfPlay

import game_stats_tree

g = Game()

runtime = SelfPlay(g)
runtime.play()

game_stats_tree = game_stats_tree.Node()
update_game_stats(game_stats_tree, runtime.log)