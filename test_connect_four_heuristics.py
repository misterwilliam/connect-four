import unittest

from game import Game, DiscState
from grid import Grid

from connect_four_heuristics import *

class OnFirstMoveSelectMidColTests(unittest.TestCase):

  def test_is_first_move(self):
    grid = Grid(2, # rows
                7, # cols
                initial_value=DiscState.empty)
    self.assertEqual(3, on_first_move_select_mid_col(grid))
