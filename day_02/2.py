import re

ID_GROUPS = r"(\d*)-(\d*)" # extract start and end of ID range
REPEATING_DIGITS = r"\b(\d+)(\1+)\b" # find repeating digits in ID --> group 1 and 2 could be unequal --> verify later

id_ranges = []
with open("./day_02/input.txt") as file:
    id_ranges = [line.split(",") for line in file]
    id_ranges = id_ranges[0] # should check


invalid_id_sum = 0

for id_range in id_ranges:
    match = re.match(ID_GROUPS, id_range).groups()
    if match:
        range_start, range_end = map(int, match)
        print(f"Range: {range_start}-{range_end}:")

        for i in range(range_start, range_end + 1):
            match = re.match(REPEATING_DIGITS, str(i))
            if match:
                invalid_id_sum += i
                print(f"  Invalid ID found: {i}")

print(invalid_id_sum)