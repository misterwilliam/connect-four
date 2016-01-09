import unittest

from game import Game, DiscState
from grid import Grid

from connect_four_heuristics import *

class OnFirstMoveSelectMidColTests(unittest.TestCase):

  def test_is_first_move(self):
    grid = Grid(2, # rows
                7, # cols
                initial_value=DiscState.empty)
    self.assertEqual(3, on_first_move_select_mid_col(None, grid, [0, 1, 2, 3]))

class GetWinningMoveTests(unittest.TestCase):

  def test_no_winning_move(self):
    grid = Grid(3, 3, initial_value=DiscState.empty)
    self.assertEqual(None, get_winning_move(grid, DiscState.red))

  def test_has_winning_move(self):
    grid = Grid(2, 4,
      initial_grid=[
        [DiscState.red, DiscState.red, DiscState.red, DiscState.empty],
        [DiscState.empty, DiscState.empty, DiscState.empty, DiscState.empty],
      ])
    self.assertEqual(3, get_winning_move(grid, DiscState.red))