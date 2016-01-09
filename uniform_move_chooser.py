import random

from move_chooser import MoveChooser

class UniformMoveChooser(MoveChooser):

  def __init__(self, game_stats_tree, exploitation_rate=0.9):
    self.game_stats_tree = game_stats_tree
    self.current_node = game_stats_tree
    self.exploitation_rate = exploitation_rate

  def restart(self):
    self.current_node = self.game_stats_tree

  def request_move(self, current_player, grid, possible_moves):
    choose_random = random.random() > self.exploitation_rate
    if choose_random or \
         self.current_node is None or \
         len(self.current_node.children) == 0:
      return random.choice(possible_moves)
    else:
      scored_moves = self.score_moves(current_player, self.current_node)
      return self.select_move(scored_moves)

  def report_move(self, move):
    if self.current_node is not None and \
        move in self.current_node.children:
      self.current_node = self.current_node.children[move]
    else:
      self.current_node = None

  def score_moves(self, current_player, current_node):
    move_scores = []
    for move, child in current_node.children.items():
      num_wins = child.win_counts.get(current_player, 0)
      total = sum(child.win_counts.values())
      move_scores.append((move, num_wins / total))
    return move_scores

  def select_move(self, scored_moves):
    total_score = sum(score for move, score in scored_moves)
    acc = 0
    random_num = random.uniform(0, total_score)
    for move, score in scored_moves:
      acc += score
      if random_num <= acc:
        return move
    else:
      assert False