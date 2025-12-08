
with open("./day_03/input.txt") as file:
    banks = file.read().splitlines()

total_joltage = 0

for bank in banks:
    stack = []
    to_remove = len(bank) - 12

    for battery in bank:

        # Use a stack to maintain a sequence with the largest possible value in each slot/digit spot of the final joltage value
        # Remove smaller battery joltages if we still have values to remove, i.e. don't need all remaining batteries for the digit count
        while stack and to_remove > 0 and stack[-1] < battery:
            stack.pop()
            to_remove -= 1
        stack.append(battery)

    if to_remove > 0:
        stack = stack[:-to_remove]

    current_joltage = "".join(stack)
    total_joltage += int(current_joltage)
    
print(total_joltage)