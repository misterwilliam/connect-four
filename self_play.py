import random

from game import Game, DiscState

class SelfPlay:

  def __init__(self, move_chooser):
    self.move_chooser = move_chooser

  def play(self, game):
    self.game = game
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

  def calc_move(self, current_player):
    if self.game.current_player is DiscState.red:
      return self.find_best_move(self.game.current_player)
    else:
      return random.randint(0, self.game.grid.width)

  def find_best_move(self, color):
    return self.move_chooser.request_move(
      self.game.current_player,
      [move for move in range(self.game.grid.width)])
