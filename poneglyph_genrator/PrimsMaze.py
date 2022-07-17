from random import randint
import numpy as np


class Cell:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.left = True
        self.up = True
        self.down = True
        self.right = True
        self.is_visited = False

    def __repr__(self):
        return f"<{self.x}, {self.y}>, <←: {self.left}, ↑: {self.up}, →: {self.right}, ↓: {self.down}>"


def get_walls(cell: Cell, x, y):
    walls = []
    if cell.left and cell.x != 0:
        walls.append((cell, (-1, 0), 0))
    if cell.up and cell.y != 0:
        walls.append((cell, (0, -1), 1))
    if cell.right and cell.x != x - 1:
        walls.append((cell, (1, 0), 2))
    if cell.down and cell.y != y - 1:
        walls.append((cell, (0, 1), 3))
    return walls


def get_connected_cell(wall, cells):
    cell_a = wall[0]
    cell_b = cells[wall[0].x + wall[1][0], wall[0].y + wall[1][1]]
    return cell_a, cell_b


def connect(cell_a: Cell, cell_b: Cell, direction):
    if direction == 0:
        cell_a.left = False
        cell_b.right = False
    elif direction == 1:
        cell_a.up = False
        cell_b.down = False
    elif direction == 2:
        cell_a.right = False
        cell_b.left = False
    elif direction == 3:
        cell_a.down = False
        cell_b.up = False
    cell_a.is_visited = True
    cell_b.is_visited = True


def generate_prims_maze(x, y, x0, y0):
    cells = np.array([[Cell(i, j) for j in range(0, y)] for i in range(0, x)])
    wall_list = []
    random_cell = cells[randint(0, x0), randint(0, y0)]
    random_cell.is_visited = True
    wall_list.extend(get_walls(random_cell, x, y))
    while len(wall_list) != 0:
        index = randint(0, len(wall_list) - 1)
        wall = wall_list.pop(index)
        cell_a, cell_b = get_connected_cell(wall, cells)
        if not (cell_a.is_visited and cell_b.is_visited):
            connect(cell_a, cell_b, wall[2])
            wall_list.extend(get_walls(cell_b, x, y))
    return cells
