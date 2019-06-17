# 직사각형 미로를 가정한다.
# 재귀함수 'find_path'의 이해를 돕기 위해 지역변수를 최소한으로 줄임
labyrinth = ''    # 미로
i_length = 0           # 미로의 세로길이
j_length = 0           # 미로의 가로길이
all_paths = []    # 시작점에서 도착점까지의 모든 경로를 저장할 리스트

def main():
    global i_length
    global j_length
    si, sj = get_labyrinth()        # 시작점의 i, j 좌표
    i_length = len(labyrinth)
    j_length = len(labyrinth[0])
    find_path([], si, sj)
    print_labyrinth()

def find_path(path, i, j):   # path는 지금까지 거쳐온 좌표를 저장, i, j는 현재 위치
    visited = (i, j) in path     # 왔던길인지 판별
    wall = (i == i_length) or (j == j_length) or (i == -1) or (j == -1)    # 벽인지 판별

    # 다음 두 조건은 and의 앞뒤가 바뀌면 IndexError발생
    not_way = not wall and labyrinth[i][j] == 'x'    # 길이 아님
    arrived = not wall and labyrinth[i][j] == 'd'    # 목적지에 도달함

    if wall or not_way or visited:  # 벽에 막혔거나 길이 아니거나 왔던길이라면
        return    # 직전 좌표로 돌아감

    if arrived:    # 목적지에 도착했다면
        path.append((i, j))
        all_paths.append(path)
        return

    find_path(path+[(i, j)], i+1, j)  # 하
    find_path(path+[(i, j)], i, j+1)  # 우
    find_path(path+[(i, j)], i-1, j)  # 상
    find_path(path+[(i, j)], i, j-1)  # 좌

def get_labyrinth():
    global labyrinth
    with open("미로.txt", "r") as f:
        labyrinth = f.read()    # 파일을 하나의 문자열로 읽어들임
    labyrinth = [i.split() for i in labyrinth.split('\n')]    # labyrinth를 2차원 리스트로 변환
    for i in range(len(labyrinth)):
        try:
            sj = labyrinth[i].index('s')
            si = i
            break
        except ValueError:
            continue
    return si, sj

def print_labyrinth():
    for each_path in all_paths:
        for i in range(i_length):
            for j in range(j_length):
                if labyrinth[i][j] == 's':
                    print('☆', end=' ')
                elif labyrinth[i][j] == 'd':
                    print('★', end=' ')
                elif (i, j) in each_path:
                    print('■', end=' ')
                elif labyrinth[i][j] == 'o':
                    print('□', end=' ')
                elif labyrinth[i][j] == 'x':
                    print('▩', end=' ')
                else:
                    print('?', end=' ')
            print()
        print()

if __name__ == "__main__":
    main()


#

