import random
import time
import numpy as np

from tile import Tile


class Disk:
    def __init__(self, CELL_SIZE, FIELD_SIZE, TILE_SIZE):
        self.CELL_SIZE = CELL_SIZE
        self.FIELD_SIZE = FIELD_SIZE
        self.TILE_SIZE = TILE_SIZE
        self.black_count = 0
        self.white_count = 0
        self.grid = [[0] * FIELD_SIZE for _ in range(FIELD_SIZE)]

        self.grid[int(FIELD_SIZE / 2 - 1)][int(FIELD_SIZE / 2 - 1)] = 2
        self.grid[int(FIELD_SIZE / 2)][int(FIELD_SIZE / 2)] = 2
        self.grid[int(FIELD_SIZE / 2 - 1)][int(FIELD_SIZE / 2)] = 1
        self.grid[int(FIELD_SIZE / 2)][int(FIELD_SIZE / 2 - 1)] = 1

        self.VALID_DIR = [[0, 1], [1, 1], [1, 0], [1, -1],
                          [0, -1], [-1, -1], [-1, 0], [-1, 1]]

        self.player_go = True

    @staticmethod
    def other_tile(color):
        if color == "black":
            return 2
        else:
            return 1

    @staticmethod
    def this_tile(color):
        if color == "black":
            return 1
        else:
            return 2

    def is_on_board(self, row, col):
        return 0 <= row < self.FIELD_SIZE and 0 <= col < self.FIELD_SIZE

    def is_valid_move(self, row, col, color):
        if not self.is_on_board(row, col):
            return False
        if self.grid[row][col] != 0:
            return False
        for direction in self.VALID_DIR:
            temp = [row + direction[0], col + direction[1]]
            while 0 <= temp[0] <= self.FIELD_SIZE - 1 and \
                    0 <= temp[1] <= self.FIELD_SIZE - 1 and \
                    self.grid[temp[0]][temp[1]] == self.other_tile(color):
                temp[0] += direction[0]
                temp[1] += direction[1]
                if self.is_on_board(temp[0], temp[1]) and \
                        self.grid[temp[0]][temp[1]] == self.this_tile(color):
                    return True
        return False

    def flip(self, row, col, color, direction):
        temp = [row + direction[0], col + direction[1]]
        while self.grid[temp[0]][temp[1]] == self.other_tile(color):
            self.grid[temp[0]][temp[1]] = self.this_tile(color)
            temp[0] += direction[0]
            temp[1] += direction[1]
        return

    def has_valid_move(self, color):
        return len(self.get_valid_move(color)) != 0

    def tile_move(self, row, col, color):
        if self.is_valid_move(row, col, color):
            self.grid[row][col] = self.this_tile(color)
            for direction in self.VALID_DIR:
                temp = [row + direction[0], col + direction[1]]
                while 0 <= temp[0] < self.FIELD_SIZE and \
                        0 <= temp[1] < self.FIELD_SIZE:
                    if self.grid[temp[0]][temp[1]] == 0:
                        break
                    if self.grid[temp[0]][temp[1]] == \
                            self.this_tile(color):
                        self.flip(row, col, color, direction)
                        break
                    temp[0] += direction[0]
                    temp[1] += direction[1]
                    if self.has_valid_move("white"):
                        self.player_go = False
                        print("ai go")

    def ai_move(self):
        time.sleep(0.2)
        if self.player_go is False:
            if self.get_valid_move("white") != []:
                move = random.choice(self.get_valid_move("white"))
                self.tile_move(move[0], move[1], "white")
                if self.has_valid_move("black"):
                    self.player_go = True
                    print("player go")

    def draw_tiles(self):
        x, y = 0, 0
        for row in range(self.FIELD_SIZE):
            for col in range(self.FIELD_SIZE):
                if self.grid[row][col] == 1:
                    Tile(self.TILE_SIZE,
                         self.CELL_SIZE,
                         x, y, "black"
                         ).draw_tile()
                elif self.grid[row][col] == 2:
                    Tile(self.TILE_SIZE,
                         self.CELL_SIZE,
                         x, y, "white"
                         ).draw_tile()
                x += self.CELL_SIZE
            y += self.CELL_SIZE
            x = 0

    def get_valid_move(self, color):
        valid_moves = []
        for x in range(self.FIELD_SIZE):
            for y in range(self.FIELD_SIZE):
                if self.is_valid_move(x, y, color):
                    valid_moves.append([x, y])
        return valid_moves

    def game_ends(self):
        self.white_count, self.black_count = 0, 0
        for row in range(self.FIELD_SIZE):
            for col in range(self.FIELD_SIZE):
                if self.grid[row][col] == 1:
                    self.black_count += 1
                if self.grid[row][col] == 2:
                    self.white_count += 1
        if not self.has_valid_move("white") and \
                not self.has_valid_move("black"):
            return True
        elif (self.black_count != 0 and self.white_count == 0) or \
                (self.black_count == 0 and self.white_count != 0):
            return True
        elif self.white_count + self.black_count == 64:
            return True
        return False

    def winner(self):
        if self.game_ends():
            print("BLACK: ", self.black_count)
            print("WHITE: ", self.white_count)
            textSize(50)
            fill(255, 0, 0)
            text("BLACK: " + str(self.black_count), 150, 100)
            text("WHITE: " + str(self.white_count), 150, 200)
            text("Click the board to enter", 150, 400)
            text("your name", 150, 500)
            if self.black_count > self.white_count:
                print("Black wins")
                textSize(50)
                fill(255, 0, 0)
                text("BLACK WINS", 150, 300)
            elif self.black_count == self.white_count:
                print("A tie.")
                textSize(50)
                fill(255, 0, 0)
                text("A TIE", 150, 300)
            else:
                print("White wins")
                textSize(50)
                fill(255, 0, 0)
                text("WHITE WINS", 150, 300)
