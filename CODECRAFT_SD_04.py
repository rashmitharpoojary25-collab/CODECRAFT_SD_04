#SUDOKU SOLVER

import math

def find_empty(g, n):
    for i in range(n):
        for j in range(n):
            if g[i][j] == 0:
                return i, j
    return None

def valid(g, r, c, num, n):
    if num in g[r]:
        return False
    for i in range(n):
        if g[i][c] == num:
            return False

    size = int(math.sqrt(n))
    sr = (r // size) * size
    sc = (c // size) * size

    for i in range(sr, sr + size):
        for j in range(sc, sc + size):
            if g[i][j] == num:
                return False
    return True

def solve(g, n):
    pos = find_empty(g, n)
    if not pos:
        return True
    r, c = pos

    for num in range(1, n + 1):
        if valid(g, r, c, num, n):
            g[r][c] = num
            if solve(g, n):
                return True
            g[r][c] = 0
    return False

n = int(input("Enter grid size (e.g., 3, 4, 9): "))
grid = []
print("Enter the grid row by row (use 0 for empty cells):")

for _ in range(n):
    grid.append(list(map(int, input().split())))

if solve(grid, n):
    print("Solved Sudoku:")
    for row in grid:
        print(*row)
else:
    print("No solution exists")