with open("투표결과.txt", "r") as file:
    names = file.read().split()
for name in set(names):
    print(name, names.count(name))

