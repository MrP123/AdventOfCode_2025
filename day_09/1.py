from itertools import combinations
import numpy as np

with open("./day_09/input.txt") as file:
    red_tiles = file.read().splitlines()

red_tiles = np.asarray([np.asarray(red_tile.split(","), dtype=int) for red_tile in red_tiles])

max_area = 0

for (x1, y1), (x2, y2) in combinations(red_tiles, 2):
    dx = np.abs(x2 - x1) + 1
    dy = np.abs(y2 - y1) + 1
    area = dx * dy

    if area > max_area:
        max_area = area

print(max_area)