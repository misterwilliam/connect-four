from game import DiscState

class Node:

  def __init__(self, children=None, win_counts=None):
    self.children = {} if children is None else children
    self.win_counts = {} if win_counts is None else win_counts

def update_game_stats(root, log, winner):
  if winner is None:
    return
  current_node = root
  for col in log:
    if col in current_node.children:
      child = current_node.children[col]
      child.win_counts[winner] = child.win_counts.get(winner, 0) + 1
      current_node = child
    else:
      child = Node(win_counts={})
      child.win_counts[winner] = child.win_counts.get(winner, 0) + 1
      current_node.children[col] = child
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