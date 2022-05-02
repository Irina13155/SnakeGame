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
        x = random.randrange(2, self.width_w // 10 - 10) * 10
        y = random.randrange(2, self.height_w // 10 - 10) * 10
        print(x, y)
        return self.canvas.create_rectangle(x, y, x + 10, y + 10, fill='red')

    def get_position(self):
        return self.canvas.coords(self.nutrition)


class Snake:
    def __init__(self, canvas, width_w, height_w):
        self.canvas = canvas
        self.width_w = width_w
        self.height_w = height_w
        head = self.canvas.create_rectangle(self.width_w/10, self.height_w/10, self.width_w/10 + 10, self.height_w/10 + 10, fill='green')
        self.direction = "Left"
        self.eating_food = False
        self.snake_body = [head]

    def get_head_position(self):
        return self.canvas.coords(self.snake_body[0])

    def get_position(self, item):
        return self.canvas.coords(item)

    def kill_snake(self):
        self.canvas.delete(tk.ALL)

    def create_head(self):
        vector_direction = {
            "Left": [-10, 0],
            "Right": [10, 0],
            "Up": [0, -10],
            "Down": [0, 10]
        }
        coords = self.get_head_position()
        x = vector_direction[self.direction][0] + coords[0]
        y = vector_direction[self.direction][1] + coords[1]
        head = self.canvas.create_rectangle(x, y, x + 10, y + 10, fill='green')
        self.snake_body.insert(0, head)

    def step(self):
        self.create_head()
        if self.eating_food is False:
            self.canvas.delete(self.snake_body[-1])
            self.snake_body.pop(-1)
        else:
            self.eating_food = False

        if len(self.snake_body) > 1:
            coords = self.get_position(self.snake_body[1])
            self.canvas.delete(self.snake_body[1])
            self.snake_body[1] = self.canvas.create_rectangle(coords[0], coords[1], coords[2], coords[3], fill='white')

    def check_biting(self):
        coords = self.get_head_position()
        if len(self.snake_body) > 3:
            for block in self.snake_body[3:-1]:
                coords_block = self.get_position(block)
                if coords[0] == coords_block[0] and \
                    coords[1] == coords_block[1]:
                    print(coords)
                    print(coords_block)
                    return True


class Model:
    canvas = None
    width_w = 400
    height_w = 300

    def __init__(self, root):
        root.geometry('400x340')
        root.configure(background="white")
        self.canvas = tk.Canvas(root, width=self.width_w, height=self.height_w)
        exit_button = tk.Button(root, text="Exit", command=root.destroy)
        exit_button.place(x=5, y=310)
        self.canvas.pack(side=tk.TOP)
        self.game = True
        self.snake = Snake(self.canvas, self.width_w, self.height_w)
        self.food = Food(self.canvas, self.width_w, self.height_w)
        x = threading.Thread(target=self.cycle_move)
        x.start()
        self.score = 0

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
        if self.snake.check_biting() is True:
            self.game_over()

    def game_over(self):
        self.snake.kill_snake()
        self.game = False
        self.canvas.create_text(self.width_w/2, self.height_w/2, text='You Lose. Game Over.')

    def check_food(self):
        coord_food = self.food.get_position()
        coord_snake = self.snake.get_head_position()
        if [coord_food[0], coord_food[1]] == [coord_snake[0], coord_snake[1]]:
            self.score += 1
            self.snake.eating_food = True
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


