from disk import Disk


CELL_SIZE = 100
TILE_SIZE = 80
FIELD_SIZE = 8
CELL_COLOR = (0, 100, 0)
STROKE_WEIGHT = 1.5
game_over = False
used = False


def setup():
    global d
    size(CELL_SIZE * FIELD_SIZE, CELL_SIZE * FIELD_SIZE)
    d = Disk(CELL_SIZE, FIELD_SIZE, TILE_SIZE)
    x, y = 0, 0
    for row in d.grid:
        for col in row:
            fill(*CELL_COLOR)
            strokeWeight(STROKE_WEIGHT)
            rect(x, y, CELL_SIZE, CELL_SIZE)
            x += CELL_SIZE
        y += CELL_SIZE
        x = 0


def draw():
    global game_over
    d.draw_tiles()
    d.ai_move()
    d.game_ends()
    d.winner()
    if d.game_ends():
        game_over = True


def mousePressed():
    row = mouseY / CELL_SIZE
    col = mouseX / CELL_SIZE
    d.tile_move(row, col, "black")
    output()


def input(message=''):
    from javax.swing import JOptionPane
    return JOptionPane.showInputDialog(frame, message)


def output():
    global game_over, used
    if game_over and not used:
        answer = input('enter your name')
        if answer:
            print('hi ' + answer)
        elif answer == '':
            print('[empty string]')
        else:
            print(answer)
        score = d.black_count
        unsorted_score_file = open('unsorted_scores.txt', 'a+')
        unsorted_score_file.readlines()
        unsorted_score_file.write(answer + " " + str(score) + "\n")
        unsorted_score_file.close()
        with open("unsorted_scores.txt") as f1:
            lines = f1.readlines()
            sorted_lines = sorted(lines,
                                  key=lambda line: int(line.split()[-1]),
                                  reverse=True)
            with open("scores.txt", "w+") as f2:
                for line in sorted_lines:
                    f2.write(line)
        used = True
