from game import Game
from textual_runtime import TextualRuntime

g = Game()

runtime = TextualRuntime(g)
runtime.start()
