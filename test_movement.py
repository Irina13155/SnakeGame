import tkinter as tk
import threading
import time


class Rectangle:

    width_w = 600
    height_w = 400
    canvas = None

    def __init__(self, root):
        self.canvas = tk.Canvas(root, width=self.width_w, height=self.height_w)
        self.canvas.pack()
        x1, y1 = self.width_w//2, self.height_w//2
        self.c1 = self.canvas.create_rectangle(x1, y1, x1 + 10, y1 + 10, fill='black')
        self.game = True
        self.direction = "Left"
        root.bind_all("<Key>", self.keypress)

    def get_position(self):
        return self.canvas.coords(self.c1)

    def check_collision(self):
        coords = self.get_position()
        if coords[0] < 1 or coords[1] < 1 or coords[2] > self.width_w-1 or coords[3] > self.height_w-1:
            self.canvas.delete(self.c1)
            self.game = False
            self.canvas.create_text(300, 200, text='You Lose. Game Over.')

    def move(self):
        while self.game is True:
            if self.direction == "Left":
                self.canvas.move(self.c1, - 10, 0)
            elif self.direction == "Right":
                self.canvas.move(self.c1, + 10, 0)
            elif self.direction == "Up":
                self.canvas.move(self.c1, 0, -10)
            elif self.direction == "Down":
                self.canvas.move(self.c1, 0, +10)

            time.sleep(0.1)
            self.check_collision()

    def keypress(self, event):

        if self.game is True:
            if event.char == "a":
                self.direction = "Left"
            elif event.char == "d":
                self.direction = "Right"
            elif event.char == "w":
                self.direction = "Up"
            elif event.char == "s":
                self.direction = "Down"


if __name__ == '__main__':
    root = tk.Tk()
    rectangle = Rectangle(root)
    x = threading.Thread(target=rectangle.move)
    x.start()
    root.mainloop()


