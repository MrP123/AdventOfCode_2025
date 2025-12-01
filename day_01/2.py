
AMT_CLICKS = 100

current_click = 50
amt_zero_clicks = 0

with open("./day_01/input.txt") as file:
    
    for line in file:
        line = line.strip()

        direction = -1 if line[0] == "L" else +1 # only L or R in input data
        clicks = int(line[1:])

        # Just handle one click at a time and check immediately afterwards
        for _ in range(clicks):
            current_click = (current_click + direction * 1) % AMT_CLICKS
            if current_click == 0:
                amt_zero_clicks += 1

        # Initial approach with accumulating clicks and then adjusting --> does not fully work, switched to above
        # current_click = current_click + direction * clicks
        #   
        # handled = False
        # while current_click >= AMT_CLICKS:
        #     current_click -= AMT_CLICKS
        #     amt_zero_clicks += 1
        #     handled = True
        # 
        # while current_click < 0:
        #     current_click += AMT_CLICKS
        #     amt_zero_clicks += 1
        #     handled = True
        # 
        # if current_click == 0 and not handled:
        #     amt_zero_clicks += 1

print(amt_zero_clicks)