import tkinter as tk
import random
import time
import threading


class Food:
    def __init__(self, canvas, width_w, height_w):
        self.canvas = canvas
        self.width_w = width_w
        self.height_w = height_w
        self.nutrition = self.create_food()

    def create_food(self):
        x = random.randrange(20, self.width_w // 10) * 10
        y = random.randrange(20, self.height_w // 10) * 10
        return self.canvas.create_rectangle(x, y, x + 10, y + 10, fill='red')

    def get_position(self):
        return self.canvas.coords(self.nutrition)


class Snake:
    def __init__(self, canvas, width_w, height_w):
        self.canvas = canvas
        self.width_w = width_w
        self.height_w = height_w
        self.head = self.canvas.create_rectangle(self.width_w/2, self.height_w/2, self.width_w/2 + 10, self.height_w/2 + 10, fill='green')

    def get_position(self):
        return self.canvas.coords(self.head)

class Model:
    canvas = None
    width_w = 600
    height_w = 400

    def __init__(self, root):
        self.canvas = tk.Canvas(root, width=self.width_w, height=self.height_w)
        self.canvas.pack()
        self.snake = Snake(self.canvas, self.width_w, self.height_w)
        self.game = True
        self.direction = "Left"
        self.food = Food(self.canvas, self.width_w, self.height_w)
        x = threading.Thread(target=self.move)
        x.start()

    def get_position(self, item):
        return self.canvas.coords(item)

    def check_collision(self):
        coords = self.snake.get_position()
        if coords[0] < 0 or coords[1] < 0 or coords[2] > self.width_w or coords[3] > self.height_w:
            self.canvas.delete(self.snake)
            self.game = False
            self.canvas.create_text(300, 200, text='You Lose. Game Over.')

    def move(self):
        while self.game is True:
            if self.direction == "Left":
                self.canvas.move(self.snake.head, - 10, 0)
            elif self.direction == "Right":
                self.canvas.move(self.snake.head, + 10, 0)
            elif self.direction == "Up":
                self.canvas.move(self.snake.head, 0, -10)
            elif self.direction == "Down":
                self.canvas.move(self.snake.head, 0, +10)

            time.sleep(0.1)
            self.check_food()
            self.check_collision()

    def check_food(self):
        coord_food = self.food.get_position()
        coord_snake = self.snake.get_position()
        if [coord_food[0], coord_food[1]] == [coord_snake[0], coord_snake[1]]:
            self.canvas.delete(self.food.nutrition)
            self.food = Food(self.canvas, self.width_w, self.height_w)

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


