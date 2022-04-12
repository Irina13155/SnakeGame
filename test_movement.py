import tkinter as tk


class Rectangle:

    def __init__(self, root):
        self.width_w, self.height_w = 600, 400
        self.canvas = tk.Canvas(root, width=self.width_w, height=self.height_w)
        self.canvas.pack()
        x1, y1 = self.width_w//2, self.height_w//2
        self.c1 = self.canvas.create_rectangle(x1, y1, x1 + 10, y1 + 10, fill='black')
        self.status = True
        root.bind_all("<Key>", self.keypress)

    def get_position(self):
        return self.canvas.coords(self.c1)

    def check_collision(self):
        coords = self.get_position()
        if coords[0] < 0 or coords[1] < 0 or coords[2] > self.width_w or coords[3] > self.height_w:
            self.canvas.delete(self.c1)
            self.status = False
            self.canvas.create_text(300, 200, text='You Lose! Game Over!')

    def keypress(self, event):
        if self.status is True:
            x = 0
            y = 0
            if event.char == "a":
                x = -10
            elif event.char == "d":
                x = 10
            elif event.char == "w":
                y = -10
            elif event.char == "s":
                y = 10
            self.canvas.move(self.c1, x, y)
            self.check_collision()


if __name__ == '__main__':
    root = tk.Tk()
    rectangle = Rectangle(root)
    root.mainloop()


