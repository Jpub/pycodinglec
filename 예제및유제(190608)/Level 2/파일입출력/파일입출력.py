"""
file = open("output1.txt", "w")
file.write("print()와 write()에는 어떤 차이가 있을까?")
file.close()

with open("output1.txt", "a") as file:
    file.write("write()는 줄바꿈이 되지 않는다는 것이 다르다.")

"""

file = open("output1.txt", "a")
file.write("\n이렇게 하면\n줄바꿈이\n된다.\n")
file.close()

