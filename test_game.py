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

  def test_is_in_connected_diag_down(self):
    g = Game(initial_grid=Grid(3, 3,
      initial_grid=[[DiscState.red, DiscState.black, DiscState.empty],
                    [DiscState.red, DiscState.red, DiscState.empty],
                    [DiscState.black, DiscState.red, DiscState.red]]))
    self.assertTrue(g.is_in_connected_diag_down(Point(1, 1), 3))
    g = Game(initial_grid=Grid(3, 3,
      initial_grid=[[DiscState.red, DiscState.black, DiscState.empty],
                    [DiscState.red, DiscState.red, DiscState.empty],
                    [DiscState.black, DiscState.red, DiscState.black]]))
    self.assertFalse(g.is_in_connected_diag_down(Point(1, 1), 3))

  def test_is_in_connected_diag_up(self):
    g = Game(initial_grid=Grid(3, 3,
      initial_grid=[[DiscState.red, DiscState.black, DiscState.red],
                    [DiscState.black, DiscState.red, DiscState.empty],
                    [DiscState.red, DiscState.red, DiscState.black]]))
    self.assertTrue(g.is_in_connected_diag_up(Point(1, 1), 3))
    g = Game(initial_grid=Grid(3, 3,
      initial_grid=[[DiscState.red, DiscState.black, DiscState.black],
                    [DiscState.black, DiscState.red, DiscState.empty],
                    [DiscState.red, DiscState.red, DiscState.black]]))
    self.assertFalse(g.is_in_connected_diag_up(Point(1, 1), 3))
