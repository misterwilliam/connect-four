import unittest

from game import Game, DiscState
from grid import Grid, Point

class GameTest(unittest.TestCase):

  def test_add_disc(self):
    game = Game()
    game.add_disc(0, DiscState.red)
    game.add_disc(0, DiscState.red)
    game.add_disc(0, DiscState.red)
    game.add_disc(0, DiscState.red)
    game.add_disc(0, DiscState.red)
    game.add_disc(0, DiscState.red)
    with self.assertRaises(ValueError):
      game.add_disc(0, DiscState.red)

  def test_has_discs_in_a_row_has_horiz(self):
    g = Game(initial_grid=Grid(3, 3,
      initial_grid=[[DiscState.empty, DiscState.empty, DiscState.empty],
                    [DiscState.empty, DiscState.empty, DiscState.empty],
                    [DiscState.red, DiscState.red, DiscState.red]]))
    self.assertTrue(g.has_connected_discs(Point(2, 1), row_size=3))
    g = Game(initial_grid=Grid(3, 3,
      initial_grid=[[DiscState.empty, DiscState.empty, DiscState.empty],
                    [DiscState.empty, DiscState.empty, DiscState.empty],
                    [DiscState.red, DiscState.red, DiscState.black]]))
    self.assertFalse(g.has_connected_discs(Point(2, 1), row_size=3))
