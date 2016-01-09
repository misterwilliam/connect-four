from game import DiscState

class Node:

  def __init__(self, children=None, win_counts=None):
    self.children = {} if children is None else children
    self.win_counts = {} if win_counts is None else win_counts
    self.play_counts = 0 if win_counts is None else sum(win_counts.values())

  def __eq__(self, other):
    if self.children != other.children:
      print(1)
      return False
    if self.win_counts != other.win_counts:
      print(2)
      return False
    if self.play_counts != other.play_counts:
      print(3)
      return False
    return True

  def __repr__(self):
    str_repr = "Node(children: %s win_counts: %s play_counts: %i)" % (
        self.children, self.win_counts, self.play_counts
    )
    return str_repr

  def record_win(self, winner):
    self.play_counts += 1
    if winner is not None:
      self.win_counts[winner] = self.win_counts.get(winner, 0) + 1

def update_game_stats(root, log, winner):
  current_node = root
  current_node.record_win(winner)
  for col in log:
    if col in current_node.children:
      child = current_node.children[col]
    else:
      child = Node()
      current_node.children[col] = child
    child.record_win(winner)
    current_node = child

def get_num_plays_from_node(node):
  total = 0
  for move, child in node.children.items():
    total += sum(child.win_counts.values())
  return total

def print_stats(root):
  str_repr = []
  for key, child in root.children.items():
    red = child.win_counts.get(DiscState.red, 0)
    black = child.win_counts.get(DiscState.black, 0)
    str_repr.append("%i %i:%i\n" % (key, red, black))
  print("".join(str_repr) + "\n")