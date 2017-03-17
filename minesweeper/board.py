from random import randint
class Board():

    def __init__(self):
        self.board = []

    def generate(self, width, height):
        for i in range(0, height):
            self.board.append([0] * width)

        self.width  = width
        self.height = height

    def place_mines(self, num_mines):
        for i in range(0, num_mines):
            self.place_mine()

    def place_mine(self):
        rand_x, rand_y = self.generate_rand_coords()

        while self.board[rand_y][rand_x] == "*":
            rand_x, rand_y = self.generate_rand_coords()

        self.board[rand_y][rand_x] = "*"

    def generate_rand_coords(self):
        rand_x = randint(0, self.width - 1)
        rand_y = randint(0, self.height - 1)
        return rand_x, rand_y

    def count_adjacent_mines_per_tile(self):
        for yidx, row in enumerate(self.board):
            for xidx, tile in enumerate(row):
                if tile == "*":
                    self.increment_tile(xidx, yidx)

    def increment_tile(self, x, y):
        surrounding_deltas = [
            [-1, -1],
            [-1,  0],
            [-1,  1],
            [ 0, -1],
            [ 0,  1],
            [ 1, -1],
            [ 1,  0],
            [ 1,  1]
        ]

        for coords in surrounding_deltas:
            xd, yd   = coords
            actual_x = xd + x
            actual_y = yd + y
            if self.are_coords_in_grid(actual_x, actual_y) and self.board[actual_y][actual_x] != "*":
              self.board[actual_y][actual_x] += 1

    def are_coords_in_grid(self, x, y):
        x_in_bounds = 0 <= x < len(self.board[0])
        y_in_bounds = 0 <= y < len(self.board)

        if x_in_bounds and y_in_bounds:
            return True
        else:
            return False
