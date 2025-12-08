
with open("./day_03/input.txt") as file:
    banks = file.read().splitlines()

total_joltage = 0

for bank in banks:
    current_max = 0
    for i in range(len(bank)):
        for j in range(i + 1, len(bank)):
            b1, b2 = bank[i], bank[j]

            current_amt = int(b1 + b2)
            if current_amt > current_max:
                current_max = current_amt

    total_joltage += current_max

print(total_joltage)