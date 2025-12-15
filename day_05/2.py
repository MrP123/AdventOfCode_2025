
with open("./day_05/input.txt") as file:
    database = file.read().splitlines()

empty_line_index = database.index("")
fresh_id_ranges = database[:empty_line_index]
# available_ids = database[empty_line_index + 1 :]

ranges = [tuple(map(int, fresh_range.split("-"))) for fresh_range in fresh_id_ranges]

ranges.sort() # sort ranges by start value --> only need to check end of current range with start of next range
merged_ranges = []
current_start, current_end = ranges[0]

for other_start, other_end in ranges[1:]:
    if other_start <= current_end + 1:  # overlap if other range starts before the current range ends 
        current_end = max(current_end, other_end) # extend the current range's end if needed
    else:
        merged_ranges.append((current_start, current_end))
        current_start, current_end = other_start, other_end # start new current range --> for loop will increment and setup next comparison

merged_ranges.append((current_start, current_end)) # add last range --> no more comparisons left so must be ok


total_amt = 0
for other_start, other_end in merged_ranges:
    # print(f"Merged range: {other_start}-{other_end}")
    amt = other_end - other_start + 1
    total_amt += amt

print(f"Total amount: {total_amt}")
