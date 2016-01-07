from enum import Enum
from itertools import takewhile

from grid import Grid, Point

import grid_utils

class DiscState(Enum):
  empty = 0
  red = 1
  black = 2

class Game(object):

  def __init__(self, initial_grid=None):
    self.restart(initial_grid)

  def restart(self, initial_grid=None):
    if initial_grid is None:
      self.grid = Grid(6, # Rows
                       7, # Cols
                       initial_value=DiscState.empty)
    else:
      self.grid = initial_grid
    self.current_player = DiscState.red
    self.winner = None
    self.is_end = False

  def try_turn(self, color, col_index):
    added_point = self.try_move(color, col_index)
    if added_point is not None:
      winner = self.get_winner(added_point, self.current_player)
      if winner:
        self.winner = winner
        self.is_end = True
        return True
      else:
        if not self.is_board_full():
          self.switch_player()
        else:
          # Tie game
          self.is_end = True
        return True
    return False

  def try_move(self, color, col_index):
    if self.current_player is not color:
      return None
    if not self.can_add_disc(col_index):
      return None
    return self.add_disc(col_index, self.current_player)

  def switch_player(self):
    if self.current_player is DiscState.red:
      self.current_player = DiscState.black
    else:
      self.current_player = DiscState.red

  def is_board_full(self):
    for col_index in range(self.grid.width):
      if self.can_add_disc(col_index):
        return False
    return True

  def can_add_disc(self, col_index):
    if col_index >= self.grid.width:
      return False
    return self.grid[-1][col_index] is DiscState.empty

  def add_disc(self, col_index, color):
    for row_index in range(self.grid.height):
      if self.grid[row_index][col_index] is DiscState.empty:
        self.grid[row_index][col_index] = color
        return Point(row_index, col_index)
        break
    else:
      raise ValueError("column %i is full" % col_index)

  def get_winner(self, last_move, current_player, row_size=4):
    assert self.grid.at(last_move) is not DiscState.empty
    if grid_utils.is_in_row_run(self.grid, last_move, row_size) or \
        grid_utils.is_in_col_run(self.grid, last_move, row_size) or \
        grid_utils.is_in_diag_down_run(self.grid, last_move, row_size) or \
        grid_utils.is_in_diag_up_run(self.grid, last_move, row_size):
        return current_player
    return None

  def render_board(self):
    str_repr = ["Current board state:\n"]
    str_repr += [" %i " % col_index for col_index in range(self.grid.width)] + ["\n"]
    for row in reversed(self.grid):
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
