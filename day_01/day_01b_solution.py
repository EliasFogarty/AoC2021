filename = "day_01_input.txt"

with open(filename) as file:
    file_lines = [line.strip() for line in file]

file_length = len(file_lines)

increase = 0
window = 0
prev_window = 0

for i in range(0, file_length):

    file_lines[i] = int(file_lines[i])

    prev_window = window

    if i > 1:
        window = file_lines[i] + file_lines[i-1] + file_lines[i-2]

        if i > 2:
            if window > prev_window:
                increase += 1

print (increase)