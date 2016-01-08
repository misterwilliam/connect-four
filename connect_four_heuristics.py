from game import DiscState

import grid_utils

def on_first_move_select_mid_col(current_player, grid, possible_moves):
  if grid_utils.is_row_all(grid, 0, DiscState.empty):
    middle = int(grid.width / 2)
    if middle in possible_moves:
      return middle
  return None