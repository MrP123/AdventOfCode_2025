from itertools import combinations
import numpy as np

with open("./day_08/input.txt") as file:
    junction_boxes = file.read().splitlines()

# junction_boxes = [np.asarray(junction_box.split(","), dtype=int) for junction_box in junction_boxes]

print(*junction_boxes, sep="\n")

distances = []
for i, j in combinations(range(len(junction_boxes)), 2):
    delta = junction_boxes[i] - junction_boxes[j]
    distance = np.linalg.norm(delta)
    distances.append((distance, i, j))
distances = np.asarray(distances) # handling of indices i/j as float is suboptimal but works apparently

distances = distances[np.argsort(distances[:, 0])] # sort by distance to get closest first for connection
distances = distances[:1000] # Consider only the 1000 shortest distances

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
        # update all junction boxes in circuit_j to circuit_i as they are connected now
        for k in circuits:
            if circuits[k] == circuit_j:
                circuits[k] = circuit_i


circuit_lengths = {}
for k, v in circuits.items():
    # only count non-zero circuits, i.e. the non default ones
    if v != 0:
        circuit_lengths[v] = circuit_lengths.get(v, 0) + 1

    # print(f"Junction box {junction_boxes[k]} is in circuit {v}")

circuit_lengths_sorted = sorted(circuit_lengths.values(), reverse=True)
result = np.prod(circuit_lengths_sorted[:3])
print(result)