from grid import Point

def run_len(grid, path, value):
  """Returns the number of continous elements along path that have value |value|"""
  num_matches = 0
  for point in path:
    if grid.at(point) is value:
      num_matches += 1
    else:
      break
  return num_matches

def gen_straight_path(grid, start, step, max_length):
  """Yields a path of points starting from |start| up to length |max_length| with each
  step |step| from the previous one. All points guaranteed to be inside of |grid|."""
  for i in range(max_length):
    next_point = Point(start.row + step.row * i, start.col + step.col * i)
    if grid.is_inside(next_point):
      yield next_point

def is_in_row_run(grid, point, length):
  start_state = grid.at(point)
  num_matches_left = run_len(grid,
                             gen_straight_path(grid,
                                               Point(point.row, point.col - 1),
                                               Point(0, -1),
                                               length - 1),
                             start_state)
  num_matches_right = run_len(grid,
                              gen_straight_path(grid,
                                                Point(point.row, point.col + 1),
                                                Point(0, 1),
                                                length - 1),
                              start_state)
  return num_matches_left + num_matches_right >= length - 1

def is_in_col_run(grid, point, length):
  start_state = grid.at(point)
  num_matches_down = run_len(grid,
                             gen_straight_path(grid,
                                               Point(point.row - 1, point.col),
                                               Point(-1, 0),
                                               length - 1),
    start_state)
  num_matches_up = run_len(grid,
                           gen_straight_path(grid,
                                             Point(point.row + 1, point.col),
                                             Point(1, 0),
                                             length - 1),
    start_state)
  return num_matches_down + num_matches_up >= length - 1