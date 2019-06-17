def main():
    n = int(input("n: "))
    line = [1]
    print_ant(line)
    for i in range(n-1):
        line = get_next_line(line)
        print_ant(line)

def print_ant(line):
    for j in line:
        print(j, end='')
    print()

def get_next_line(previous_line):
    next_line = []
    i = 0
    while i < len(previous_line):
        j = i+1
        next_line.append(previous_line[i])
        while True:
            if j == len(previous_line) or previous_line[i] != previous_line[j]:
                # or 앞뒤에 있는 조건의 위치를 바꾸면 IndexError 발생
                next_line.append(j-i)
                i = j
                break
            j += 1
    return next_line

if __name__ == "__main__":
    main()


