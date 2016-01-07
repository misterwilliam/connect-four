import abc

class Runtime(metaclass=abc.ABCMeta):

  @abc.abstractmethod
  def __init__(self, game, move_chooser):
    self.game = game
    self.move_chooser = move_chooser

  @abc.abstractmethod
  def start(self):
    pass