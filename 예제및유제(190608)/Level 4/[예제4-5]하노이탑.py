def hanoi(disks, starting_point, tool, destination):
    if disks == 0:
        return
    hanoi(disks-1, starting_point, destination, tool)
    print(starting_point, "->", destination)
    hanoi(disks-1, tool, starting_point, destination)


n = int(input("n: "))
hanoi(n, 'A', 'B', 'C')

