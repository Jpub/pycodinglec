def reverse(i):
    if i == -1:
        return      # 베이스 케이스
    print(string[i], end='')
    reverse(i-1)             # 재귀호출

string = input("문자열: ")
reverse(len(string)-1)

