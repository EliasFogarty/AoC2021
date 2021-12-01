filename = "day_01_input.txt"

with open(filename) as file:
    file_lines = [line.strip() for line in file]

file_length = len(file_lines)

increase = 0

for i in range(0, file_length):

    file_lines[i] = int(file_lines[i])

    if i > 0:
        if file_lines[i] > file_lines[i-1]:
            increase += 1

print (increase)