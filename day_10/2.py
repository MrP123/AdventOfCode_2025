from itertools import combinations

with open("./day_10/simple_input.txt") as file:
    machine_status = file.read().splitlines()

mapping = {".": 0, "#": 1}

for machine in machine_status:
    entries = machine.split(" ")

    lights = entries[0][1:-1]
    lights = list(map(mapping.get, lights))

    light_binary = 0
    for light in lights[::-1]: # Reverse to match binary order of buttons
        light_binary = (light_binary << 1) | light        

    buttons = entries[1:-1]
    buttons = [b[1:-1] for b in buttons]
    buttons = [list(map(int, b.split(","))) for b in buttons]

    buttons_binary = []
    for button_comb in buttons:
        button_binary = sum([2**button for button in button_comb])
        buttons_binary.append(button_binary)

    joltage = entries[-1][1:-1]
    joltage = joltage.split(",")
    joltage = list(map(int, joltage))

    amt_joltage_counters = len(joltage)
    joltages_even_odd = [j % 2 for j in joltage]
    joltage_binary = 0
    for j in joltages_even_odd[::-1]: # Reverse to match binary order of buttons
        joltage_binary = (joltage_binary << 1) | j

    print(f"{joltage} --> {joltage_binary:0{amt_joltage_counters}b}")
    
    # print(f"Lights: {lights}, Buttons: {buttons}")
    # print(f"Light binary: {light_binary:04b}, Light decimal: {light_binary}")
    # print(f"Buttons binary: {[f'{b:04b}' for b in buttons_binary]}, Buttons decimal: {buttons_binary}")

    possible_combinations = []

    joltages_start = 0 # 0b0000
    joltage_state = joltages_start
    for comb_length in range(1, len(buttons_binary)+1): # check with fewest combinations first
        for test_buttons in combinations(buttons_binary, comb_length):
            for button in test_buttons:
                joltage_state ^= button

            if joltage_state == joltage_binary:
                print(f"  Found solution with buttons {test_buttons} of lenght {len(test_buttons)}")
                possible_combinations.append(test_buttons)

            joltage_state = joltages_start

    for comb in possible_combinations:
        print(f"    Combination: {comb}")
        
        for comb_length in range(1, len(comb)+1): # check with fewest combinations first
            for test_buttons in combinations(comb, comb_length):
                full_joltages = [0 for _ in range(amt_joltage_counters)]

                for i in range(20):
                    for button in test_buttons:
                        # push button
                        for j in range(amt_joltage_counters):
                            if (button >> j) & 1:
                                full_joltages[j] += 1

                    if full_joltages == joltage:
                        print(f"      Found full joltages after {i+1} presses: {full_joltages}")
                        break
                
                print(f"      After {i+1} presses: {full_joltages}")
    
    # only test first machine for now
    break


# (3) = 8
# (1, 3) = 10
# (2) = 4
# (2, 3) = 12
# (0, 2) = 5
# (0, 1) = 3

# 0 0 0 0
# 1 0 1 0 --> (0, 2)
# 2 0 2 0 --> (0, 2)
# 3 0 3 0 --> (0, 2)
# 3 1 3 1 --> (1, 3)
# 3 2 3 2 --> (1, 3)
# 3 3 3 3 --> (1, 3)
# 3 4 3 4 --> (1, 3)
# 3 5 3 5 --> (1, 3)
# 3 5 4 6 --> (2, 3)
# 3 5 4 7 --> (3)

# 3 5 4 7
