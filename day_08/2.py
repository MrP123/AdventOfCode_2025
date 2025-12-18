from itertools import combinations
import numpy as np

with open("./day_08/input.txt") as file:
    junction_boxes = file.read().splitlines()

junction_boxes = [np.asarray(junction_box.split(","), dtype=int) for junction_box in junction_boxes]

# print(*junction_boxes, sep="\n")

distances = []
for i, j in combinations(range(len(junction_boxes)), 2):
    delta = junction_boxes[i] - junction_boxes[j]
    distance = np.linalg.norm(delta)
    distances.append((distance, i, j))
distances = np.asarray(distances) # handling of indices i/j as float is suboptimal but works apparently

distances = distances[np.argsort(distances[:, 0])] # sort by distance to get closest first for connection
# distances = distances[:1000] # Consider only the 1000 shortest distances

circuits = {i: 0 for i in range(len(junction_boxes))}
max_circuit_id = 0

for distance, i, j in distances:
    circuit_i, circuit_j = circuits[i], circuits[j]

    # Both not yet in a circuit
    if circuit_i == 0 and circuit_j == 0:
        max_circuit_id += 1
        new_circuit = max_circuit_id

        circuits[i] = new_circuit
        circuits[j] = new_circuit
    
    # Merge circuits
    elif circuit_i == 0:
        circuits[i] = circuit_j
    elif circuit_j == 0:
        circuits[j] = circuit_i

    # Both in different circuits
    elif circuit_i != circuit_j:
        for k in circuits:
            if circuits[k] == circuit_j:
                circuits[k] = circuit_i

    # final connection was just made this iteration of i/j
    if len(set(circuits.values())) == 1:
        jb1, jb2 = junction_boxes[int(i)], junction_boxes[int(j)]
        result = jb1[0] * jb2[0]
        print(f"Result = {result}")
        break