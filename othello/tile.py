class Tile:
    def __init__(self, TILE_SIZE, CELL_SIZE, x, y, color):
        self.TILE_SIZE = TILE_SIZE
        self.CELL_SIZE = CELL_SIZE
        self.x = x
        self.y = y
        self.color = color

    def draw_tile(self):
        if self.color == "black":
            fill(0)
        elif self.color == "white":
            fill(255)
        stroke(0)
        strokeWeight(2)
        circle(self.x + self.CELL_SIZE / 2,
               self.y + self.CELL_SIZE / 2,
               self.TILE_SIZE)
