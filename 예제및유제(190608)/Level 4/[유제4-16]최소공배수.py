a = int(input("a: "))
b = int(input("b: "))
if a > b:
    a, b = b, a    # a가 b보다 작은 값을 갖도록 조정
  
for i in range(1, a+1):
    if b*i % a == 0:
        print(b*i)
        break


