import random

from game import Game, DiscState
from runtime import Runtime

class SelfPlay(Runtime):

  def __init__(self, game_factory, move_chooser):
    super().__init__(game_factory, move_chooser)

  def start(self, num_iterations):
    for i in range(num_iterations):
      pass

  def play(self):
    self.game = self.game_factory()
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
