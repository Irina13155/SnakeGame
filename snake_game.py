import tkinter as tk
import random
import time
import threading


class Model:
    canvas = None
    width_w = 600
    height_w = 400

    def __init__(self, root):
        self.canvas = tk.Canvas(root, width=self.width_w, height=self.height_w)
        self.snake = self.canvas.create_rectangle(300, 200, 310, 210, fill='green')
        self.canvas.pack()
        self.game = True
        self.direction = "Left"
        self.food = self.create_food()
        x = threading.Thread(target=self.move)
        x.start()

    def create_food(self):
        x = random.randrange(20, self.width_w // 10) * 10
        y = random.randrange(20, self.height_w // 10) * 10
        return self.canvas.create_rectangle(x, y, x + 10, y + 10, fill='red')

    def get_position(self, item):
        return self.canvas.coords(item)

    def check_collision(self):
        coords = self.get_position(self.snake)
        if coords[0] < 1 or coords[1] < 1 or coords[2] > self.width_w - 1 or coords[3] > self.height_w - 1:
            self.canvas.delete(self.snake)
            self.game = False
            self.canvas.create_text(300, 200, text='You Lose. Game Over.')

    def move(self):
        while self.game is True:
            if self.direction == "Left":
                self.canvas.move(self.snake, - 10, 0)
            elif self.direction == "Right":
                self.canvas.move(self.snake, + 10, 0)
            elif self.direction == "Up":
                self.canvas.move(self.snake, 0, -10)
            elif self.direction == "Down":
                self.canvas.move(self.snake, 0, +10)

            time.sleep(0.1)
            self.check_food()
            self.check_collision()

    def check_food(self):
        coord_food = self.get_position(self.food)
        coord_snake = self.get_position(self.snake)
        if [coord_food[0], coord_food[1]] == [coord_snake[0], coord_snake[1]]:
            self.canvas.delete(self.food)
            self.food = self.create_food()


class Controller:

    def __init__(self, model):
        root.bind_all("<Key>", self.keypress)

    def keypress(self, event):
        if model.game is True:
            if event.char == "a":
                model.direction = "Left"
            elif event.char == "d":
                model.direction = "Right"
            elif event.char == "w":
                model.direction = "Up"
            elif event.char == "s":
                model.direction = "Down"


if __name__ == '__main__':
    root = tk.Tk()
    model = Model(root)
    controller = Controller(model)
    root.mainloop()


