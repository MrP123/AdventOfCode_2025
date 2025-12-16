import numpy as np

with open("./day_07/input.txt") as file:
    manifold = file.read().splitlines()

mapping = {".": 0, "S": 1, "^": 2, "|": 3}
inverse_map = {v: k for k, v in mapping.items()}

manifold = np.array([[mapping[char] for char in line] for line in manifold])

start_index = np.nonzero(manifold == mapping["S"])
manifold[start_index[0], start_index[1]] = mapping["|"] # replace start with beam --> unifys logic for propagation
start_row = start_index[0].item() # convert to int

amt_splits = 0

for i in range(len(manifold[start_row:, :]) - 1):
    top_row = manifold[start_row + i, :]
    bottom_row = manifold[start_row + i + 1, :]

    bottom_row_copy = bottom_row.copy()
    for j, (top, bot) in enumerate(zip(top_row, bottom_row)):
        if top == mapping["|"]:
            if bot == mapping["^"]:
                bottom_row_copy[j-1] = mapping["|"]
                bottom_row_copy[j+1] = mapping["|"]
                amt_splits += 1
            if bot == mapping["."]:
                bottom_row_copy[j] = mapping["|"]
    
    manifold[start_row + i + 1, :] = bottom_row_copy

    # print("".join([inverse_map[elem] for elem in current_row]))
    # print("".join([inverse_map[elem] for elem in below_row_copy]))
    # print("\n")

print(np.vectorize(inverse_map.get)(manifold))
print(f"Amount of splits: {amt_splits}")