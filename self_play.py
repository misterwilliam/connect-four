import random

from game import Game, DiscState

class SelfPlay:

  def __init__(self, game_stats):
    self.game_stats = game_stats

  def play(self, game):
    self.game = game
    self.current_node = self.game_stats
    self.log = []

    num_fails = 0
    while not self.game.is_end:
      col_index = self.calc_move(self.game.current_player)
      if self.game.can_add_disc(col_index):
        success = self.game.try_turn(self.game.current_player, col_index)
        assert success
        self.log.append(col_index)
        if self.current_node is not None and col_index in self.current_node.children:
          self.current_node = self.current_node.children[col_index]
        else:
          self.current_node = None
        num_fails = 0
      else:
        num_fails += 1
        if num_fails > 100:
          print(col_index)
          self.game.render_board()
          raise Error("Stucking searching for move")


  def calc_move(self, current_player):
    if self.game.current_player is DiscState.red:
      return self.find_best_move(self.game.current_player)
    else:
      return random.randint(0, self.game.grid.width)

  def find_best_move(self, color):
    choose_random = random.random() > 0.5
    if choose_random or \
         self.current_node is None or \
         len(self.current_node.children) == 0:
      return random.randint(0, self.game.grid.width)
    else:
      best_move_score, best_move = 0, -1
      for col_index, child in self.current_node.children.items():
        wins = child.data.get(color, 0)
        total = sum(child.data.values())
        if wins / total >= best_move_score:
          best_move = col_index
          best_move_score = wins / total
      assert best_move != -1
      return best_move
