from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])

class Grid:

  def __init__(self, height, width,
               initial_value=None, initial_grid=None):
    self.height = height
    self.width = width
    if initial_grid is None:
      self.grid = []
      for _ in range(self.height):
        row = [initial_value for _ in range(self.width)]
        self.grid.append(row)
    else:
      self.grid = initial_grid
    assert len(self.grid) == self.height
    for row in self.grid:
      assert len(row) == self.width

  def __getitem__(self, row_index):
    return self.grid[row_index]

  def gen_path_left(self, row_start_index, col_start_index, max_length):
    for i, j in self._gen_path(row_start_index, col_start_index, 0, -1, max_length):
      yield i, j

  def gen_path_right(self, row_start_index, col_start_index, max_length):
    for i, j in self._gen_path(row_start_index, col_start_index, 0, 1, max_length):
      yield i, j

  def gen_path_up(self, row_start_index, col_start_index, max_length):
    for i, j in self._gen_path(row_start_index, col_start_index, -1, 0, max_length):
      yield i, j

  def gen_path_down(self, row_start_index, col_start_index, max_length):
    for i, j in self._gen_path(row_start_index, col_start_index, 1, 0, max_length):
      yield i, j

  def _gen_path(self, row_start_index, col_start_index, row_step, col_step, max_length):
    for i in range(max_length):
      row_index = row_start_index + row_step * i
      col_index = col_start_index + col_step * i
      if 0 <= row_index < self.width and \
          0 <= col_index < self.height:
        yield (row_index, col_index)
      else:
        break

  def at(self, point):
    return self.grid[point.x][point.y]

  def is_inside(self, point):
    return 0 <= point.x < self.width and 0 <= point.y < self.height

  def visit(self, start, step, length):
    for i in range(length):
      next_point = Point(start.x + step.x * i, start.y + step.y * i)
      if self.is_inside(next_point):
        yield next_point