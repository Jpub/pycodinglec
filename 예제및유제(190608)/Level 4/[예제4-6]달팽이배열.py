# 출력: 달팽이 배열
# 입력: 정사각 달팽이 배열의 가로/세로 길이
# direction: 방향 -> d로 표현

def main():
    n = int(input("n: "))
    snail = [[0 for j in range(n)] for i in range(n)]
    i, j = 0, -1            # 반복문 첫 작동시 (0, 0)에서 시작되도록 설정
    value = 1
    i_d, j_d = 0, +1    # 시작은 우측방향 진행
    while value <= n**2:
        i += i_d      # 진행
        j += j_d
        if i == n or j == n or snail[i][j] != 0:
            i -= i_d  # 진행 취소
            j -= j_d
            i_d, j_d = d(i_d, j_d)      # 방향 전환
        else:
            snail[i][j] = value
            value += 1
    print_snail(snail, n)

def d(i_d, j_d):   # 시계방향으로 진행 방향이 바뀌도록 조절
    if i_d == 0 and j_d == +1: return (+1, 0)           # 우->하
    elif i_d == +1 and j_d == 0: return (0, -1)         # 하->좌
    elif i_d == 0 and j_d == -1: return (-1, 0)         # 좌->상
    elif i_d == -1 and j_d == 0: return (0, +1)         # 상->우

def print_snail(snail, n):
    for i in range(n):
        for j in range(n): print("%4d" % snail[i][j], end='')
        print()

if __name__ == "__main__":
    main()

