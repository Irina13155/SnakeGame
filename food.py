import random


class Food:
    def __init__(self, canvas, width_w, height_w):
        self.canvas = canvas
        self.width_w = width_w
        self.height_w = height_w
        self.object_food = self.create_object()

    def create_object(self):
        x = random.randrange(2, self.width_w // 10 - 10) * 10
        y = random.randrange(2, self.height_w // 10 - 10) * 10
        return self.canvas.create_rectangle(x, y, x + 10, y + 10, fill='red')

    def get_position(self):
        return self.canvas.coords(self.object_food)

    def delete_food(self):
        self.canvas.delete(self.object_food)
