from collections import namedtuple

Point = namedtuple('Point', ['row', 'col'])

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

  def __reversed__(self):
    return reversed(self.grid)

  def gen_path(self, start, step, length):
    for i in range(length):
      next_point = Point(start.row + step.row * i, start.col + step.col * i)
      if self.is_inside(next_point):
        yield next_point

  def at(self, point):
    return self.grid[point.row][point.col]

  def is_inside(self, point):
    return 0 <= point.row < self.height and 0 <= point.col < self.width
