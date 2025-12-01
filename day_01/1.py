
AMT_CLICKS = 100

current_click = 50
amt_zero_clicks = 0

with open("./day_01/input.txt") as file:
    
    for line in file:
        line = line.strip()

        direction = -1 if line[0] == "L" else +1 # only L or R in input data
        clicks = int(line[1:])
        
        current_click = (current_click + direction * clicks) % AMT_CLICKS
        
        if current_click == 0:
            amt_zero_clicks += 1

print(amt_zero_clicks)