from enum import Enum
from itertools import takewhile

from grid import Grid, Point

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

  def add_disc(self, col_index, color):
    for row_index in range(self.grid.height):
      if self.grid[row_index][col_index] is DiscState.empty:
        self.grid[row_index][col_index] = color
        break
    else:
      raise ValueError("column %i is full" % col_index)

  def has_connected_discs(self, start_point, row_size=4):
    start_state = self.grid.at(start_point)
    if start_state is not DiscState.empty:
      return self._has_discs_in_a_row_horiz(start_point, row_size) or \
        self._has_discs_in_a_row_vert(start_point, row_size)
    else:
      return False

  def _has_discs_in_a_row_vert(self, start_point, length=4):
    start_state = self.grid.at(start_point)
    if start_state is DiscState.empty:
      return False
    num_matches = 0
    for point in takewhile(lambda point: self.grid.at(point) is start_state,
                       self.grid.visit(Point(start_point.x + 1, start_point.y),
                                       Point(1, 0),
                                       length - 1)):
      num_matches += 1
    for point in takewhile(lambda point: self.grid.at(point) is start_state,
                       self.grid.visit(Point(start_point.x - 1, start_point.y),
                                       Point(-1, 0),
                                       length - 1)):
      num_matches += 1
    return num_matches >= length - 1

  def _has_discs_in_a_row_horiz(self, start_point, length=4):
    start_state = self.grid.at(start_point)
    if start_state is DiscState.empty:
      return False
    num_matches = 0
    for point in takewhile(lambda point: self.grid.at(point) is start_state,
                           self.grid.visit(Point(start_point.x, start_point.y + 1),
                                           Point(0, 1),
                                           length - 1)):
      num_matches += 1
    for point in takewhile(lambda point: self.grid.at(point) is start_state,
                           self.grid.visit(Point(start_point.x, start_point.y - 1),
                                           Point(0, -1),
                                           length - 1)):
      num_matches += 1
    return num_matches >= length - 1
