from game import DiscState
from runtime import Runtime

class CompareRuntime(Runtime):

  def __init__(self, game, move_chooser_a, move_chooser_b, num_iters):
    self.game = game
    self.move_chooser_a = move_chooser_a
    self.move_chooser_b = move_chooser_b
    self.num_iters = num_iters

  def start(self):
    a_wins = 0
    b_wins = 0
    for i in range(self.num_iters):
      winner = self.play(self.move_chooser_a, self.move_chooser_b)
      if winner is DiscState.red:
        a_wins += 1
      winner = self.play(self.move_chooser_b, self.move_chooser_a)
      if winner is DiscState.red:
        b_wins += 1
    return a_wins, b_wins

  def play(self, first_player_move_chooser, second_player_move_chooser):
    self.game.restart()
    first_player_move_chooser.restart()
    second_player_move_chooser.restart()

    num_fails = 0
    while not self.game.is_end:
      if self.game.current_player is DiscState.red:
        col_index = first_player_move_chooser.request_move(
          self.game.current_player,
         [move for move in range(self.game.grid.width)])
      else:
        col_index = second_player_move_chooser.request_move(
          self.game.current_player,
         [move for move in range(self.game.grid.width)])
      if self.game.can_add_disc(col_index):
        success = self.game.try_turn(self.game.current_player, col_index)
        assert success

        first_player_move_chooser.report_move(col_index)
        second_player_move_chooser.report_move(col_index)
        num_fails = 0
      else:
        num_fails += 1
        if num_fails > 100:
          print(col_index)
          self.game.render_board()
          raise Error("Stucking searching for move")

    return self.game.winner