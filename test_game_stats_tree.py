import unittest

from game_stats_tree import *

class UpdateGameStatsTests(unittest.TestCase):

  def test_winner_with_empty_tree(self):
    root = Node()
    log = [1, 2, 3]
    update_game_stats(root, log, "red")
    expected_game_stats_tree = Node(
      children={
        1: Node(
          children={
            2: Node(
              children={
                3: Node(
                    win_counts={
                      "red": 1
                    }
                  )
              },
              win_counts={
                "red": 1
              }
            )
          },
          win_counts={
            "red": 1
          }
        )
      },
      win_counts={
        "red": 1
      }
    )
    self.assertEqual(expected_game_stats_tree, root)

  def test_winner_with_nonempty_tree(self):
    root = Node(
      children={
        1: Node(
          children={
            2: Node(
              children={
                3: Node(
                    win_counts={
                      "red": 1
                    }
                  )
              },
              win_counts={
                "red": 1
              }
            )
          },
          win_counts={
            "red": 1
          }
        )
      },
      win_counts={
        "red": 1
      }
    )
    log = [1, 2, 2]
    update_game_stats(root, log, "red")

    expected_game_stats_tree = Node(
      children={
        1: Node(
          children={
            2: Node(
              children={
                2: Node(
                    win_counts={
                      "red": 1
                    }
                  ),
                3: Node(
                    win_counts={
                      "red": 1
                    }
                  )
              },
              win_counts={
                "red": 2
              }
            )
          },
          win_counts={
            "red": 2
          }
        )
      },
      win_counts={
        "red": 2
      }
    )
    self.assertEqual(expected_game_stats_tree, root)