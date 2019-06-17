# 출력: 달팽이 배열
# 입력: 정사각 달팽이 배열의 가로/세로 길이
# direction: 방향 -> d로 표현
# cancel: 최소 -> c로 표현
def main():
    n = int(input("n: "))
    snail = [[0 for j in range(n)] for i in range(n)]
    make_snail(snail, 0, 0, 0, 1, 1, n)
    print_snail(snail, n)

def make_snail(snail, i, j, i_d, j_d, value, n):
    if value > n**2:
        return
    elif i == n or j == n or snail[i][j] != 0:
        i_c, j_c = i_d, j_d
        i_d, j_d = d(i_d, j_d)
        make_snail(snail, i-i_c+i_d, j-j_c+j_d, i_d, j_d, value, n)
    else:
        snail[i][j] = value
        make_snail(snail, i+i_d, j+j_d, i_d, j_d, value+1, n)

def d(i_d, j_d):   # 시계방향으로 진행 방향이 바뀌도록 조절
    if i_d == 0 and j_d == +1: return (+1, 0)           #우->하
    elif i_d == +1 and j_d == 0: return (0, -1)          #하->좌
    elif i_d == 0 and j_d == -1: return (-1, 0)          #좌->상
    elif i_d == -1 and j_d == 0: return (0, +1)         #상->우

def print_snail(snail, n):
    for i in range(n):
        for j in range(n):
            print("%4d" % snail[i][j], end='')
        print()

if __name__ == "__main__":
    main()

