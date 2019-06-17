def get_previous_line(line):
    previous_line = ''
    for i in range(0, len(line), 2):
        previous_line += line[i]*int(line[i+1])
    return previous_line

line = input("n번째 행: ")
print(get_previous_line(line))
