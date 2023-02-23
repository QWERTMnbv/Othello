from tile import Tile


def test_constructor():
    tile1 = Tile(20, 4, 3, 4, "black")
    assert tile1.CELL_SIZE == 4
    assert tile1.TILE_SIZE == 20
    assert tile1.x == 3
    assert tile1.y == 4
    assert tile1.color == "black"
