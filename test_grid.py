import unittest

import grid

class GridTests(unittest.TestCase):

  def test_init(self):
    g = grid.Grid(3, 2)
    self.assertEqual([[None, None],
                      [None, None],
                      [None, None]],
                     g.grid)

  def test_init_with_initial_grid(self):
    g = grid.Grid(3, 2, initial_grid=[["RED", "RED"],
                                      ["RED", "RED"],
                                      ["RED", "RED"]])
    self.assertEqual([["RED", "RED"],
                      ["RED", "RED"],
                      ["RED", "RED"]],
                     g.grid)

  def test_set(self):
    g = grid.Grid(3, 2)
    g[0][1] = "RED"
    self.assertEqual([[None, "RED"],
                      [None, None],
                      [None, None]],
                     g.grid)
