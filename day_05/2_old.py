#Initial attempt to solve part 2 --> does not work! --> kept as references

with open("./day_05/input.txt") as file:
    database = file.read().splitlines()

empty_line_index = database.index("")
fresh_id_ranges = database[:empty_line_index]
# available_ids = database[empty_line_index + 1 :]

ranges = [tuple(map(int, fresh_range.split("-"))) for fresh_range in fresh_id_ranges]

ranges_to_consider = ranges.copy()
iteration = 0
while True:
    iteration += 1

    has_changed = False

    for i, (start, end) in enumerate(ranges_to_consider):

        for j, (start_cmp, end_cmp) in enumerate(ranges_to_consider):
            if i == j or (start_cmp, end_cmp) == (None, None) or (start, end) == (None, None):
                continue

            if start <= start_cmp <= end_cmp <= end:
                # print("Full overlap!")
                # print(f"Range {start}-{end} is fully contained in {start_cmp}-{end_cmp}")
                ranges_to_consider[i] = (None, None) # should probably pop immediately?
                has_changed = True
                break

            elif start <= start_cmp <= end <= end_cmp:
                # print("Partial overlap on right!")
                # print(f"Range {start}-{end} is partially overlapped by {start_cmp}-{end_cmp}")
                overlamp_amount = end - start_cmp + 1
                # print(f"Overlapped amount: {overlamp_amount}")
                # print(f"Valid range is {start}-{end - overlamp_amount}")

                ranges_to_consider[i] = (start, end - overlamp_amount)
                has_changed = True
                break

            elif start_cmp <= start <= end_cmp <= end:
                # print("Partial overlap on left!")
                # print(f"Range {start}-{end} is partially overlapped by {start_cmp}-{end_cmp}")
                overlamp_amount = end_cmp - start + 1
                # print(f"Overlapped amount: {overlamp_amount}")
                # print(f"Valid range is {start + overlamp_amount}-{end}")

                ranges_to_consider[i] = (start + overlamp_amount, end)
                has_changed = True
                break

        # else:
        #     non_overlapping_ranges.append((start, end))

    ranges_to_consider = [r for r in ranges_to_consider if r != (None, None)]

    if not has_changed:
        print(f"No changes made, breaking loop after iteration {iteration}.")
        break
    else:
        print(f"Iteration {iteration} complete, continuing...")

print("Ranges to consider after removing overlaps:")
total_amt = 0
for start, end in ranges_to_consider:
    amt = end - start + 1
    total_amt += amt

print(f"Total amount: {total_amt}")