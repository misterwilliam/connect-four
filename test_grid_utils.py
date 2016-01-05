from unittest import TestCase

from grid import Grid, Point
from grid_utils import *

class RunLenTests(TestCase):

  def test_run_len_zero(self):
    g = Grid(3, 3, initial_value=1)
    path = [Point(0, 0), Point(0, 1), Point(0, 2)]
    self.assertEqual(0, run_len(g, path, 0))

  def test_run_len_part_of_path(self):
    g = Grid(2, 3,
             initial_grid=[[1, 1, 0],
                           [0, 0, 0]])
    path = [Point(0, 0), Point(0, 1), Point(0, 2)]
    self.assertEqual(2, run_len(g, path, 1))

  def test_run_len_full_path(self):
    g = Grid(2, 3,
             initial_grid=[[1, 1, 1],
                           [0, 0, 0]])
    path = [Point(0, 0), Point(0, 1), Point(0, 2)]
    self.assertEqual(3, run_len(g, path, 1))

class GenStraightPath(TestCase):

  def test_zero_length_path(self):
    g = Grid(3, 3)
    path = [point for point in gen_straight_path(g, Point(0, 0), Point(1, 1), 0)]
    self.assertEqual([], path)

  def test_path_inside_grid(self):
    g = Grid(3, 3)
    path = [point for point in gen_straight_path(g, Point(0, 0), Point(0, 1), 3)]
    self.assertEqual([Point(0, 0), Point(0, 1), Point(0, 2)], path)