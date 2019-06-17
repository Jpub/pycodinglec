import itertools
string = input("순서를 섞을 문자열: ")
print(list(itertools.permutations(string, len(string))))

#
