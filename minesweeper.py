#create a function that takes a grid of '#' and '-', where each hash(#) represents a mine and each dash(-) represents a mine free spot
#return a grid where each dash is replaced by a digit indicating the number of mines immediately adjacent to that spot

def count_mines(grid):
    rows = len(grid)
    cols = len(grid[0])
    new_grid = [[0 for j in range(cols)] for i in range(rows)]
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == "#":
                new_grid[i][j] = "#"
                continue
            count = 0
            for r in range(max(0, i-1), min(rows, i+2)):
                for c in range(max(0, j-1), min(cols, j+2)):
                    if grid[r][c] == "#":
                        count += 1
            new_grid[i][j] = str(count)
    return new_grid
grid = [
    ["-", "-", "-", "#"],
    ["-", "#", "-", "-"],
    ["-", "-", "-", "-"],
    ["#", "-", "-", "-"]
]

new_grid = count_mines(grid)
for row in new_grid:
    print(row)