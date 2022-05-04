from snake import Direction
from model import Model


class Controller:

    def __init__(self, root):
        self.model = Model(root)
        root.bind_all("<Key>", self.keypress)

    def keypress(self, event):
        if self.model.game is True:
            if event.char == "a":
                self.model.snake.direction = Direction.LEFT
            elif event.char == "d":
                self.model.snake.direction = Direction.RIGHT
            elif event.char == "w":
                self.model.snake.direction = Direction.UP
            elif event.char == "s":
                self.model.snake.direction = Direction.DOWN
