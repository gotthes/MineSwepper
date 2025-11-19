import random


def create_minesweeper_field():
    positions = list(range(100))
    mine_positions = random.sample(positions, 40)

    field = [[0 for _ in range(10)] for _ in range(10)] #поле 10х10

    for pos in mine_positions:
        row = pos // 10
        col = pos % 10
        field[row][col] = 1

    return field

def print_field(field):
    for i, row in enumerate(field):
        for cell in row:
            if cell == 1:
                print("X", end=" ")  #мина
            else:
                print(".", end=" ")  #пустая клетка
        print()


field = create_minesweeper_field()
print_field(field)
