# Runtime for managing the interactive component of the game. Allows user to play the game
# through a text based interface.

from game import DiscState

class TextualRuntime:

  def __init__(self, game):
    self.game = game
    self.state = {
      "continue": True
    }

  def start(self):
    while self.state["continue"]:
      self.render()
      self.eval(self.get_input())

    if self.game.winner is not None:
      self.render()
      print("The winner is: %s" % self.disc_state_to_player_name(self.game.winner))

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
        self.game.try_turn(self.game.current_player, col_index)
    if self.game.is_end:
      self.state["continue"] = False

  def disc_state_to_player_name(self, disc_state):
    if disc_state is DiscState.red:
      return "O"
    else:
      return "X"
