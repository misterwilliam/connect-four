import random

from game import Game, DiscState

class SelfPlay:

  def __init__(self, game):
    self.game = game

  def play(self):
    while self.game.winner is None:
      col_index = self.calc_move(self.game.current_player)
      if self.game.can_add_disc(col_index):
        success = self.game.try_turn(self.game.current_player, col_index)
        assert success
    self.render_board()
    print("Winner is: %s" % self.disc_state_to_player_name(self.game.winner))

  def calc_move(self, current_player):
    return random.randint(0, self.game.grid.width)

  def render_board(self):
    str_repr = [" %i " % col_index for col_index in range(self.game.grid.width)] + ["\n"]
    for row in reversed(self.game.grid):
      row_repr = []
      for disc_value in row:
        if disc_value is DiscState.empty:
          row_repr.append("| |")
        elif disc_value is DiscState.red:
          row_repr.append("|O|")
        else:  # disc_value is black
          row_repr.append("|X|")
      row_repr.append("\n")
      str_repr += row_repr
    print("".join(str_repr))

  def disc_state_to_player_name(self, disc_state):
    if disc_state is DiscState.red:
      return "O"
    else:
      return "X"