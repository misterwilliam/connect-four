def run_len(grid, path, value):
  """Returns the number of continous elements along path that have value |value|"""
  num_matches = 0
  for point in path:
    if grid.at(point) is value:
      num_matches += 1
    else:
      break
  return num_matches

def is_in_connected_row(self, point, length):
  start_state = self.grid.at(point)
  if start_state is DiscState.empty:
    return False
  num_matches_left = self.get_num_matching(
    self.grid.gen_path(Point(point.row, point.col - 1),
                       Point(0, -1),
                       length - 1),
    start_state)
  num_matches_right = self.get_num_matching(
    self.grid.gen_path(Point(point.row, point.col + 1),
                       Point(0, 1),
                       length - 1),
    start_state)
  return num_matches_left + num_matches_right >= length - 1

def is_in_connected_col(self, point, length):
  start_state = self.grid.at(point)
  if start_state is DiscState.empty:
    return False
  num_matches_down = self.get_num_matching(
    self.grid.gen_path(Point(point.row - 1, point.col),
                       Point(-1, 0),
                       length - 1),
    start_state)
  num_matches_up = self.get_num_matching(
    self.grid.gen_path(Point(point.row + 1, point.col),
                       Point(1, 0),
                       length - 1),
    start_state)
  return num_matches_down + num_matches_up >= length - 1

def is_in_connected_diag_down(self, point, length):
  start_state = self.grid.at(point)
  if start_state is DiscState.empty:
    return False
  num_matches_diag_down_right = self.get_num_matching(
    self.grid.gen_path(Point(point.row + 1, point.col + 1),
                       Point(1, 1),
                       length - 1),
    start_state)
  num_matches_diag_up_left = self.get_num_matching(
    self.grid.gen_path(Point(point.row - 1, point.col - 1),
                       Point(-1, -1),
                       length - 1),
    start_state)
  return num_matches_diag_down_right + num_matches_diag_up_left >= length - 1

def is_in_connected_diag_up(self, point, length):
  start_state = self.grid.at(point)
  if start_state is DiscState.empty:
    return False
  num_matches_diag_down_left = self.get_num_matching(
    self.grid.gen_path(Point(point.row + 1, point.col - 1),
                       Point(1, -1),
                       length - 1),
    start_state)
  num_matches_diag_up_right = self.get_num_matching(
    self.grid.gen_path(Point(point.row - 1, point.col + 1),
                       Point(-1, 1),
                       length - 1),
    start_state)
  return num_matches_diag_down_left + num_matches_diag_up_right >= length - 1