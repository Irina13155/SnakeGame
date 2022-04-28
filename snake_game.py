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
        print(x, y)
        return self.canvas.create_rectangle(x, y, x + 10, y + 10, fill='red')

    def get_position(self):
        return self.canvas.coords(self.nutrition)


class Snake:
    def __init__(self, canvas, width_w, height_w):
        self.canvas = canvas
        self.width_w = width_w
        self.height_w = height_w
        head = self.canvas.create_rectangle(self.width_w/2, self.height_w/2, self.width_w/2 + 10, self.height_w/2 + 10, fill='green')
        self.direction = "Left"
        self.snake_body = [head]

    def get_head_position(self):
        return self.canvas.coords(self.snake_body[0])

    def get_position(self, item):
        return self.canvas.coords(item)

    def kill_snake(self):
        self.canvas.delete(tk.ALL)

    def create_block(self, x, y):
        block = self.canvas.create_rectangle(x, y, x + 10, y + 10, fill='white')
        self.snake_body.append(block)

    def draw_body(self):
        coords = self.get_position(self.snake_body[-1])
        x,y = 0, 0
        if self.direction == "Left":
            x = coords[2]
            y = coords[1]
        elif self.direction == "Right":
            x = coords[0]-10
            y = coords[1]
        elif self.direction == "Up":
            x = coords[0]
            y = coords[3]
        elif self.direction == "Down":
            x = coords[0]
            y = coords[1]-10

        self.create_block(x, y)

    def step(self):

        if len(self.snake_body) > 1:
            for i in range(len(self.snake_body)-1, 0, -1):
                coords = self.get_position(self.snake_body[i-1])
                block = self.snake_body[i]
                self.canvas.moveto(block, coords[0]-1, coords[1]-1)

        if self.direction == "Left":
            self.canvas.move(self.snake_body[0], -10, 0)
        elif self.direction == "Right":
            self.canvas.move(self.snake_body[0], +10, 0)
        elif self.direction == "Up":
            self.canvas.move(self.snake_body[0], 0, -10)
        elif self.direction == "Down":
            self.canvas.move(self.snake_body[0], 0, +10)



class Model:
    canvas = None
    width_w = 600
    height_w = 400

    def __init__(self, root):
        self.canvas = tk.Canvas(root, width=self.width_w, height=self.height_w)
        self.canvas.pack()
        self.game = True
        self.snake = Snake(self.canvas, self.width_w, self.height_w)
        self.food = Food(self.canvas, self.width_w, self.height_w)
        x = threading.Thread(target=self.cycle_move)
        x.start()

    def cycle_move(self):
        while self.game is True:
            self.snake.step()
            time.sleep(0.1)
            self.check_food()
            self.check_collision()

    def check_collision(self):
        coords = self.snake.get_head_position()
        if coords[0] < 0 or coords[1] < 0 or coords[2] > self.width_w or coords[3] > self.height_w:
            self.game_over()

    def game_over(self):
        self.snake.kill_snake()
        self.game = False
        self.canvas.create_text(300, 200, text='You Lose. Game Over.')

    def check_food(self):
        coord_food = self.food.get_position()
        coord_snake = self.snake.get_head_position()
        if [coord_food[0], coord_food[1]] == [coord_snake[0], coord_snake[1]]:
            self.snake.draw_body()
            self.canvas.delete(self.food.nutrition)
            self.food.nutrition = self.food.create_food()



class Controller:

    def __init__(self, root):
        self.model = Model(root)
        root.bind_all("<Key>", self.keypress)

    def keypress(self, event):
        if self.model.game is True:
            if event.char == "a":
                self.model.snake.direction = "Left"
            elif event.char == "d":
                self.model.snake.direction = "Right"
            elif event.char == "w":
                self.model.snake.direction = "Up"
            elif event.char == "s":
                self.model.snake.direction = "Down"


if __name__ == '__main__':
    root = tk.Tk()
    controller = Controller(root)
    root.mainloop()


