import numpy as np

with open("./day_06/input.txt") as file:
    math_problem = file.read().splitlines()

nums = [list(map(int, row.split())) for row in math_problem[:-1]]
ops = math_problem[-1].split()

mapping = {
    "+": np.sum,
    "*": np.prod
}

nums = np.array(nums)

total_result = 0
for i, op in enumerate(ops):
    result = mapping[op](nums[:, i])
    total_result += result

print(total_result)