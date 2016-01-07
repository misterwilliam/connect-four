import pickle
import random

from game import Game, DiscState
from runtime import Runtime

import game_stats_tree

class SelfPlay(Runtime):

  def __init__(self, game, move_chooser, model, model_path):
    super().__init__(game, move_chooser)
    self.model = model
    self.model_path = model_path

  def start(self, num_iters):
    wins = 0
    for i in range(num_iters):
      winner = self.play()
      game_stats_tree.update_game_stats(self.model, self.log, winner)
      if winner is DiscState.red:
        wins += 1
      if i % 500 == 0 and i > 0:
        print("Runs: %i 1st player win %%: %f" % (i, wins / i))
      if i % 100000 == 0 and i > 0:
        with open(self.model_path, "wb") as pickle_file:
          pickle.dump(self.model, pickle_file)
    print("Runs: %i" % num_iters)

    with open(self.model_path, "wb") as pickle_file:
      pickle.dump(self.model, pickle_file)

  def play(self):
    self.game.restart()
    self.log = []
    self.move_chooser.restart()

    num_fails = 0
    while not self.game.is_end:
      col_index = self.calc_move(self.game.current_player)
      if self.game.can_add_disc(col_index):
        success = self.game.try_turn(self.game.current_player, col_index)
        assert success
        self.log.append(col_index)
        self.move_chooser.report_move(col_index)
        num_fails = 0
      else:
        num_fails += 1
        if num_fails > 100:
          print(col_index)
          self.game.render_board()
          raise Error("Stucking searching for move")

    return self.game.winner

  def calc_move(self, current_player):
    return self.find_best_move(self.game.current_player)

  def find_best_move(self, color):
    return self.move_chooser.request_move(
      self.game.current_player,
      [move for move in range(self.game.grid.width)])
