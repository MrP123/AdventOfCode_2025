import numpy as np

with open("./day_06/input.txt") as file:
    math_problem = file.read().splitlines()

raw_nums = math_problem[:-1]
raw_ops = math_problem[-1]

mapping = {
    "+": np.sum,
    "*": np.prod
}

# determine width of each math problem based on location of operator
column_starts = []
for i, c in enumerate(raw_ops):
    if c in ["+", "*"]:
        column_starts.append(i)
column_starts.append(len(raw_ops)+1) # captures last column

total_result = 0
for i in range(len(column_starts)-1):        
    start, end = column_starts[i], column_starts[i+1]
    order = end - start - 1
    #print(f"Column {i+1} (order {order}):")

    nums = []
    for j in range(order):
        column_string = ""
        for i, row in enumerate(raw_nums):
            column = row[start:end]
            #print(column[j])

            column_string += column[j]
        nums.append(int(column_string.strip())) # strip leading/trailing spaces --> alignment is preserved through loop

    op = raw_ops[start]
    nums = np.array(nums)
    result = mapping[op](nums)
    # print(f"  Operation: {op}, Numbers: {nums}, Result: {result}")
    total_result += result

print(total_result)