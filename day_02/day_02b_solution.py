filename = "day_02_input.txt"

with open(filename) as file:
    file_lines = [line.strip() for line in file]

x = 0
y = 0
aim = 0

for i in range(0, len(file_lines)):

    split_line = file_lines[i].split(' ')
    
    direction = (split_line[0])
    distance = int((split_line[1]))
    
    if (direction == 'forward'):
        x += distance
        y += aim * distance
    elif (direction == 'down'):
        aim += distance
    elif (direction == 'up'):
        aim -= distance
        
print(x*y)