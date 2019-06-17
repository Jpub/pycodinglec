try:
    file = open("input.txt", "r")
except FileNotFoundError:
    print("파일이 없습니다.")
else:
    print(file.read())
    file.close()

