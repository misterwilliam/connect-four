import unittest

from game import DiscState
from grid import Grid
from game_stats_tree import Node

from best_known_move_chooser import *


class BestKnownMoveChooserTests(unittest.TestCase):

  def test_simple_playthrough(self):
    grid = Grid(2, 2, initial_value=DiscState.empty)
    root = Node(children={
                  0: Node(children={
                            0: Node(win_counts={
                                      DiscState.red: 1,
                                      DiscState.black: 3,
                                    }),
                            1: Node(win_counts={
                                      DiscState.red: 5,
                                      DiscState.black: 0
                                    }),
                          },
                          win_counts={
                            DiscState.red: 6,
                            DiscState.black: 3
                          }),
                  1: Node(children={
                            0: Node(win_counts={
                                DiscState.red: 2,
                                DiscState.black: 8
                              }),
                            1: Node(win_counts={
                                DiscState.red: 3,
                                DiscState.black: 3,
                              })
                          },
                          win_counts={
                            DiscState.red: 5,
                            DiscState.black: 11
                          })
                })
    move_chooser = BestKnownMoveChooser(root)

    self.assertEqual(0, move_chooser.request_move(DiscState.red, grid, [0, 1]))
    move_chooser.report_move(0)
    self.assertEqual(1, move_chooser.request_move(DiscState.red, grid, [0, 1]))

    move_chooser.restart()

    self.assertEqual(0, move_chooser.request_move(DiscState.red, grid, [0, 1]))
    move_chooser.report_move(0)
    self.assertEqual(1, move_chooser.request_move(DiscState.red, grid, [0, 1]))