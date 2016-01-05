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
      is_connected = self.has_connected_discs(added_point)
      if is_connected:
        self.winner = color
        self.is_end = True
        return self.winner
      else:
        self.switch_player()
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

  def has_connected_discs(self, start_point, row_size=4):
    start_state = self.grid.at(start_point)
    if start_state is not DiscState.empty:
      return grid_utils.is_in_row_run(self.grid, start_point, row_size) or \
        self.is_in_connected_col(start_point, row_size) or \
        self.is_in_connected_diag_down(start_point, row_size) or \
        self.is_in_connected_diag_up(start_point, row_size)
    else:
      return False

  def is_in_connected_col(self, point, length):
    start_state = self.grid.at(point)
    if start_state is DiscState.empty:
      return False
    num_matches_down = grid_utils.run_len(
      self.grid,
      grid_utils.gen_straight_path(self.grid,
                                   Point(point.row - 1, point.col),
                                   Point(-1, 0),
                                   length - 1),
      start_state)
    num_matches_up = grid_utils.run_len(
      self.grid,
      grid_utils.gen_straight_path(self.grid,
                                   Point(point.row + 1, point.col),
                                   Point(1, 0),
                                   length - 1),
      start_state)
    return num_matches_down + num_matches_up >= length - 1

  def is_in_connected_diag_down(self, point, length):
    start_state = self.grid.at(point)
    if start_state is DiscState.empty:
      return False
    num_matches_diag_down_right = grid_utils.run_len(
      self.grid,
      grid_utils.gen_straight_path(self.grid,
                                   Point(point.row + 1, point.col + 1),
                                   Point(1, 1),
                                   length - 1),
      start_state)
    num_matches_diag_up_left = grid_utils.run_len(
      self.grid,
      grid_utils.gen_straight_path(self.grid,
                                   Point(point.row - 1, point.col - 1),
                                   Point(-1, -1),
                                   length - 1),
      start_state)
    return num_matches_diag_down_right + num_matches_diag_up_left >= length - 1

  def is_in_connected_diag_up(self, point, length):
    start_state = self.grid.at(point)
    if start_state is DiscState.empty:
      return False
    num_matches_diag_down_left = grid_utils.run_len(
      self.grid,
      grid_utils.gen_straight_path(self.grid,
                                   Point(point.row + 1, point.col - 1),
                                   Point(1, -1),
                                   length - 1),
      start_state)
    num_matches_diag_up_right = grid_utils.run_len(
      self.grid,
      grid_utils.gen_straight_path(self.grid,
                                   Point(point.row - 1, point.col + 1),
                                   Point(-1, 1),
                                   length - 1),
      start_state)
    return num_matches_diag_down_left + num_matches_diag_up_right >= length - 1
