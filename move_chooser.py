import abc
import random

class MoveChooser(metaclass=abc.ABCMeta):
  """Abstract interface for a move chooser.

  A MoveChooser is used by a Runtime to automatically choose moves. To initialize the
  state of a MoveChooser, the runtime will call restart(). Then as moves are selected the
  Runtime will call report_move(). When the Runtime wants the MoveChooser to select a
  move, it will call request_move()."""

  @abc.abstractmethod
  def report_move(self, move):
    pass

  @abc.abstractmethod
  def request_move(self, current_player, grid, possible_moves):
    pass

  @abc.abstractmethod
  def restart(self):
    pass
