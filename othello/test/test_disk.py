from disk import Disk


d = Disk(100, 8, 80)


def test_constructor():
    assert d.CELL_SIZE == 100
    assert d.FIELD_SIZE == 8
    assert d.TILE_SIZE == 80
    assert d.black_count == 0
    assert d.white_count == 0
    assert len(d.grid) == 8
    assert d.grid[3][3] == 2
    assert d.grid[3][4] == 1
    assert d.grid[0][0] == 0
    assert d.player_go is True


def test_other_tile():
    assert d.other_tile("black") == 2
    assert d.other_tile("white") == 1


def test_this_tile():
    assert d.this_tile("black") == 1
    assert d.this_tile("white") == 2


def test_is_on_board():
    assert d.is_on_board(8, 8) is False
    assert d.is_on_board(7, 7) is True
    for i in range(d.FIELD_SIZE):
        for j in range(d.FIELD_SIZE):
            assert d.is_on_board(i, j) is True


def test_is_valid_move():
    assert d.is_valid_move(3, 2, "black") is True
    assert d.is_valid_move(2, 4, "white") is True
    assert d.is_valid_move(0, 0, "black") is False
    assert d.is_valid_move(5, 7, "black") is False


def test_flip():
    d.flip(3, 3, "white", [0, 1])
    assert d.grid[3][4] == 2
    d.flip(3, 4, "black", [1, 0])
    assert d.grid[4][4] == 1


def test_has_valid_move():
    assert d.has_valid_move("black") is True
    assert d.has_valid_move("white") is True


def test_tile_move():
    d0 = Disk(100, 8, 80)
    d0.tile_move(3, 2, "black")
    assert d0.grid[3][2] == 1


def test_ai_move():
    d1 = Disk(100, 8, 80)
    d1.game_ends()
    n1 = d1.white_count
    d1.ai_move()
    d1.game_ends()
    n2 = d1.white_count
    assert n2 - n1 == 0


def test_get_valid_move():
    d2 = Disk(100, 8, 80)
    assert d2.get_valid_move("black") == [[2, 3], [3, 2], [4, 5], [5, 4]]
    assert d2.get_valid_move("white") == [[2, 4], [3, 5], [4, 2], [5, 3]]


def test_game_ends():
    d3 = Disk(100, 8, 80)
    assert d3.game_ends() is False
    d3.grid[3][3], d3.grid[4][4] = 1, 1
    assert d3.game_ends() is True
    for i in range(d3.FIELD_SIZE):
        for j in range(d3.FIELD_SIZE):
            d3.grid[i][j] = 2
    assert d3.game_ends() is True
