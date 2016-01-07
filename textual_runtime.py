# Runtime for managing the interactive component of the game. Allows user to play the game
# through a text based interface.

from game import DiscState
from runtime import Runtime

class TextualRuntime(Runtime):

  def __init__(self, game, move_chooser):
    self.game = game
    self.move_chooser = move_chooser
    self.state = {
      "continue": True
    }

  def start(self):
    while self.state["continue"]:
      while not self.game.is_end and self.state["continue"]:
        if self.game.current_player is DiscState.red:
          move = self.move_chooser.request_move(self.game.current_player,
                                                [move for move in range(self.game.grid.width)])
          success = self.game.try_turn(self.game.current_player, move)
          if success:
            self.move_chooser.report_move(move)
        else:
          self.render()
          self.eval(self.get_input())

      self.render()
      print("The winner is: %s" % self.disc_state_to_player_name(self.game.winner))
      self.game.restart()
      self.move_chooser.restart()

  def render(self):
    str_repr = ["Current board state:\n"]
    str_repr += [" %i " % col_index for col_index in range(self.game.grid.width)] + ["\n"]
    for row in reversed(self.game.grid):
      row_repr = []
      for disc_value in row:
        if disc_value is DiscState.empty:
          row_repr.append("| |")
        elif disc_value is DiscState.red:
          row_repr.append("|O|")
        else:  # disc_value is black
          row_repr.append("|X|")
      row_repr.append("\n")
      str_repr += row_repr
    print("".join(str_repr))

  def get_input(self):
    print("Current player: %s" % self.disc_state_to_player_name(self.game.current_player))
    self.move_chooser.request_move(self.game.current_player,
                                   [move for move in range(self.game.grid.width)])
    command = input("--> ")
    print("\n")
    return command

  def eval(self, command):
    tokens = command.split()
    if len(tokens) == 1:
      if tokens[0] == "quit":
        self.state["continue"] = False
      elif tokens[0].isdigit():
        col_index = int(tokens[0])
        success = self.game.try_turn(self.game.current_player, col_index)
        if success:
          self.move_chooser.report_move(col_index)

  def disc_state_to_player_name(self, disc_state):
    if disc_state is DiscState.red:
      return "O"
    else:
      return "X"
