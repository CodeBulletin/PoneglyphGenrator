import PrimsMaze


def generate_hamiltonian_cycle(x: int, y: int, x0, y0):
    if x % 2 != 0 or y % 2 != 0:
        return None
    cells = PrimsMaze.generate_prims_maze(int(x / 2), int(y / 2), x0, y0)
    directions = dict()
    i = 0
    j = 0
    n = 0
    while True:
        i_half = int(i / 2)
        j_half = int(j / 2)
        cell = cells[i_half, j_half]
        if i % 2 == 0 and j % 2 == 0:
            if cell.up:
                directions[(i, j)] = (2, (1, 0), n)  # Right
                i += 1
            else:
                directions[(i, j)] = (1, (0, -1), n)  # Up
                j -= 1
        elif i % 2 == 1 and j % 2 == 0:
            if cell.right:
                directions[(i, j)] = (3, (0, 1), n)  # Down
                j += 1
            else:
                directions[(i, j)] = (2, (1, 0), n)  # Right
                i += 1
        elif i % 2 == 1 and j % 2 == 1:
            if cell.down:
                directions[(i, j)] = (0, (-1, 0), n)  # left
                i -= 1
            else:
                directions[(i, j)] = (3, (0, 1), n)  # down
                j += 1
        elif i % 2 == 0 and j % 2 == 1:
            if cell.left:
                directions[(i, j)] = (1, (0, -1), n)  # up
                j -= 1
            else:
                directions[(i, j)] = (0, (-1, 0), n)  # left
                i -= 1
        n += 1
        if i == 0 and j == 0:
            break
    return directions
