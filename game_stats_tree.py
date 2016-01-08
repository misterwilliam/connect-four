from game import DiscState

class Node:

  def __init__(self, children=None, data=None):
    self.children = {} if children is None else children
    self.data = {} if data is None else data

def update_game_stats(root, log, winner):
  if winner is None:
    return
  current_node = root
  for col in log:
    if col in current_node.children:
      child = current_node.children[col]
      child.data[winner] = child.data.get(winner, 0) + 1
      current_node = child
    else:
      child = Node(data={})
      child.data[winner] = child.data.get(winner, 0) + 1
      current_node.children[col] = child
      current_node = child

def print_stats(root):
  str_repr = []
  for key, child in root.children.items():
    red = child.data.get(DiscState.red, 0)
    black = child.data.get(DiscState.black, 0)
    str_repr.append("%i %i:%i\n" % (key, red, black))
  print("".join(str_repr) + "\n")