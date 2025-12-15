
with open("./day_05/input.txt") as file:
    database = file.read().splitlines()

empty_line_index = database.index("")
fresh_id_ranges = database[:empty_line_index]
available_ids = database[empty_line_index + 1 :]

amt_fresh = 0

for id in available_ids:
    id = int(id)

    for fresh_range in fresh_id_ranges:
        start_str, end_str = fresh_range.split("-")
        start, end = int(start_str), int(end_str)

        if start <= id <= end:
            amt_fresh += 1
            break

print(amt_fresh)