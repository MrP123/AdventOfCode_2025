import numpy as np

with open("./day_07/input.txt") as file:
    manifold = file.read().splitlines()

# Modified mapping to allow adding up each beam's timeline
mapping = {"^": -1, ".": 0, "S": 1, "|": 1}
inverse_map = {v: k for k, v in mapping.items()}

manifold = np.array([[mapping[char] for char in line] for line in manifold])

start_index = np.nonzero(manifold == mapping["S"])
manifold[start_index[0], start_index[1]] = mapping["|"] # replace start with beam --> unifys logic for propagation
start_row = start_index[0].item() # convert to int

for i in range(len(manifold[start_row:, :]) - 1):
    top_row = manifold[start_row + i, :]
    bottom_row = manifold[start_row + i + 1, :]

    bottom_row_copy = bottom_row.copy()
    for j, (top, bot) in enumerate(zip(top_row, bottom_row)):
        if top > mapping["."]:
            if bot == mapping["^"]:
                bottom_row_copy[j-1] += top
                bottom_row_copy[j+1] += top
            if bot == mapping["."]:
                bottom_row_copy[j] += top
    
    manifold[start_row + i + 1, :] = bottom_row_copy

manifold[np.nonzero(manifold == mapping["^"])] = mapping["."] # not really necessary, as last row does not contain any "^" symbols
# print(manifold)

# last row counts how many possible ways a beam could reach the end --> sum must be amt of timelines
print(np.sum(manifold[-1, :]))