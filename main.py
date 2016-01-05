from game import Game
from self_play import SelfPlay

g = Game()

runtime = SelfPlay(g)
runtime.play()
