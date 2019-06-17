def main():
    n = int(input("n: "))
    number = ''         # 이어붙이기 기능을 쓰기 위해 number를 문자열로 정의
    for i in range(1, n+1):   # n이 3일때 '123'꼴의 문자열을 만듦
        number += str(i)
    spread(number, '')

def spread(source, destination):
    if not source:
        print(destination)
        return
    for i in range(len(source)):
        spread(source[0:i]+source[i+1:], destination+source[i])

if __name__ == "__main__":
    main()
