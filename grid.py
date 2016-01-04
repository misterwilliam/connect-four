class Grid:

  def __init__(self, height, width, initial_value=None):
    self.height = height
    self.width = width
    self.grid = []
    for _ in range(self.height):
      row = [initial_value for _ in range(self.width)]
      self.grid.append(row)

  def __getitem__(self, row_index):
    return self.grid[row_index]