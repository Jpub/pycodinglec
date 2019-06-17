def main():
    string = input("순서를 섞을 문자열: ")
    spread(string, '')

def spread(source, destination):
    if not source:
        print(destination)
        return
    for i in range(len(source)):
        spread(source[0:i]+source[i+1:], destination+source[i])

if __name__ == "__main__":
    main()


#

