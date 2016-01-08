from game import DiscState

import grid_utils

def on_first_move_select_mid_col(grid):
  if grid_utils.is_row_all(grid, 0, DiscState.empty):
    return int(grid.width / 2)
  else:
    return None