count = 0

def hanoi(disks, starting_point, tool, destination):
    global count
    if disks == 0:
        return
    hanoi(disks-1, starting_point, destination, tool)
    count += 1    # starting_point에 남은 원판 1개를 destination으로 이동하며 횟수 추가
    hanoi(disks-1, tool, starting_point, destination)

n = int(input("n: "))
hanoi(n, 'A', 'B', 'C')
print("이동횟수:", count)


