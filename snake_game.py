import tkinter as tk
import time
import threading
from food import Food
from snake import Snake
from controller import Controller

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
        self.food.delete_food()
        self.game = False
        self.canvas.create_text(self.width_w/2, self.height_w/2, text='You Lose. Game Over.')

    def check_food(self):
        coord_food = self.food.get_position()
        coord_snake = self.snake.get_head_position()
        if [coord_food[0], coord_food[1]] == [coord_snake[0], coord_snake[1]]:
            self.score += 1
            self.snake.eating_food = True
            self.food.delete_food()
            self.food = Food(self.canvas, self.width_w, self.height_w)


if __name__ == '__main__':
    root = tk.Tk()
    controller = Controller(root)
    root.mainloop()


