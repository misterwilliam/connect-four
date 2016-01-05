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
