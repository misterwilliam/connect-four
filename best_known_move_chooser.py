import random

import game_stats_tree
from move_chooser import MoveChooser

class BestKnownMoveChooser(MoveChooser):

  def __init__(self, game_stats_tree, exploitation_rate=1.0, verbose=False):
    self.game_stats_tree = game_stats_tree
    self.current_node = game_stats_tree
    self.exploitation_rate = exploitation_rate
    self.verbose = verbose

  def restart(self):
    self.current_node = self.game_stats_tree

  def request_move(self, current_player, grid, possible_moves):
    choose_random = random.random() > self.exploitation_rate
    if choose_random or \
         self.current_node is None or \
         len(self.current_node.children) == 0:
      if self.verbose:
        print("Selecting randomly")
      return random.choice(possible_moves)
    else:
      scored_moves = self.score_moves(current_player, self.current_node)
      selected_move = self.select_move(scored_moves)
      if self.verbose:
        data = [
          "%i: %.0f%% (%i)" % (move, score * 100, total)
          for move, score, total in scored_moves
        ]
        print("Selected %s" % selected_move)
        print("Move stats: (total %i)" %
          game_stats_tree.get_num_plays_from_node(self.current_node))
        print("%s" % " ".join(data))
      return selected_move

  def report_move(self, move):
    if self.current_node is not None and \
        move in self.current_node.children:
      self.current_node = self.current_node.children[move]
    else:
      self.current_node = None

  def score_moves(self, current_player, current_node):
    move_scores = []
    for move, child in current_node.children.items():
      num_wins = child.data.get(current_player, 0)
      total = sum(child.data.values())
      move_scores.append((move, num_wins / total, total))
    return move_scores

  def select_move(self, scored_moves):
    scored_moves = list(scored_moves)
    scored_moves.sort(key=lambda pair: pair[1])
    return scored_moves[-1][0]