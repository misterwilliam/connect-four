from game import DiscState
from grid import Point

import grid_utils

def on_first_move_select_mid_col(current_player, grid, possible_moves):
  if grid_utils.is_row_all(grid, 0, DiscState.empty):
    middle = int(grid.width / 2)
    if middle in possible_moves:
      return middle
  return None

def if_can_win_take_do_it(current_player, grid, possible_moves):
  return get_winning_move(grid, current_player)

def block_opponent(current_player, grid, possible_moves):
  if current_player is DiscState.red:
    return get_winning_move(grid, DiscState.black)
  else:
    return get_winning_move(grid, DiscState.red)

def get_winning_move(grid, current_player):
  for col_index in range(grid.width):
    row_index = grid_utils.get_row_of_first(grid, col_index, DiscState.empty)
    current_point = Point(row_index, col_index)
    if not grid.is_inside(current_point):
      continue

    if grid_utils.is_in_row_run(grid, current_point, 4, current_player):
      return col_index
    if grid_utils.is_in_col_run(grid, current_point, 4, current_player):
      return col_index
    if grid_utils.is_in_diag_down_run(grid, current_point, 4, current_player):
      return col_index
    if grid_utils.is_in_diag_up_run(grid, current_point, 4, current_player):
      return col_index

  else:
    return None

def heuristic_move(current_player, grid, possible_moves):
  move = on_first_move_select_mid_col(current_player, grid, possible_moves)
  if move:
    return move

  move = if_can_win_take_do_it(current_player, grid, possible_moves)
  if move:
    return move

  move = block_opponent(current_player, grid, possible_moves)
  if move:
    return move
