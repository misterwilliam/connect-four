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

  def render(self):
    str_repr = ["Current board state:\n"]
    str_repr += [" %i " % col_index for col_index in range(self.game.grid.width)]
    for row in self.game.grid:
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
    return input("--> ")

  def eval(self, command):
    tokens = command.split()
    if len(tokens) == 1:
      if tokens[0] == "quit":
        self.state["continue"] = False

