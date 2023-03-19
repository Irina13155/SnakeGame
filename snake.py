from enum import Enum


class Direction(Enum):
    LEFT = (-10, 0)
    RIGHT = (10, 0)
    UP = (0, -10)
    DOWN = (0, 10)


class Snake:
    def __init__(self, canvas, width_w, height_w):
        self.canvas = canvas
        self.width_w = width_w
        self.height_w = height_w
        head = self.canvas.create_rectangle(self.width_w/10, self.height_w/10, self.width_w/10 + 10, self.height_w/10 + 10, fill='green')
        self.direction = Direction.LEFT
        self.eating_food = False
        self.snake_body = [head]

    def get_head_position(self):
        return self.canvas.coords(self.snake_body[0])

    def get_position(self, item):
        return self.canvas.coords(item)

    def kill_snake(self):
        for block in self.snake_body:
            self.canvas.delete(block)

    def create_head(self):
        coords = self.get_head_position()
        x = self.direction.value[0] + coords[0]
        y = self.direction.value[1] + coords[1]
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
