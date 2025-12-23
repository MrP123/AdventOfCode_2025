from itertools import combinations

with open("./day_10/input.txt") as file:
    machine_status = file.read().splitlines()

mapping = {".": 0, "#": 1}

sum_fewest_presses = 0

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
    
    # print(f"Lights: {lights}, Buttons: {buttons}")
    # print(f"Light binary: {light_binary:04b}, Light decimal: {light_binary}")
    # print(f"Buttons binary: {[f'{b:04b}' for b in buttons_binary]}, Buttons decimal: {buttons_binary}")

    lights_start = 0 # 0b0000
    lights_state = lights_start    
    for comb_length in range(1, len(buttons_binary)+1): # check with fewest combinations first
        for test_buttons in combinations(buttons_binary, comb_length):
            for button in test_buttons:
                lights_state ^= button

            if lights_state == light_binary:
                # print(f"  Found solution with buttons {test_buttons} of lenght {len(test_buttons)}")
                sum_fewest_presses += len(test_buttons)
                break

            lights_state = lights_start
        
        # stupid break outer loop construct in Python
        else:
            continue
        break

print(f"Sum of fewest presses: {sum_fewest_presses}")

# ....
# .#.# --> (1, 3)
# .##. --> (2, 3)
# 
