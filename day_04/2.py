import numpy as np

with open("./day_04/input.txt") as file:
    grid = file.read().splitlines()

mapping = {".": 0, "@": 1, "x": 2}
inverse_map = {v: k for k, v in mapping.items()}

grid = np.array([[mapping[char] for char in line] for line in grid])


def get_neighbors(grid, x, y):
    neighbors = []
    for dy in [-1, 0, 1]:
        for dx in [-1, 0, 1]:
            if dy == 0 and dx == 0:
                continue

            nx, ny = x + dx, y + dy
            if 0 <= nx < grid.shape[0] and 0 <= ny < grid.shape[1]:
                neighbors.append(grid[nx, ny])

    return neighbors


new_grid = np.copy(grid)
amt_accessable = 0
prev_amt_accessable = amt_accessable - 1

while amt_accessable > prev_amt_accessable:
    prev_amt_accessable = amt_accessable

    for y in range(grid.shape[0]):
        for x in range(grid.shape[1]):
            neighbors = get_neighbors(grid, x, y)
            unique, count = np.unique(neighbors, return_counts=True)
            sum_neighbors = dict(zip(unique, count)).get(1, 0)
            # assigning 0 for a roll that was just removed and summing like previously would be faster but less pretty for printing

            if grid[x, y] == 1 and sum_neighbors < 4:
                new_grid[x, y] = 2
                amt_accessable += 1

    grid = np.copy(new_grid)
    # print("Current state:")
    # print(np.vectorize(inverse_map.get)(new_grid))

print(amt_accessable)
