n = int(input("n: "))
prime_number = True
for i in range(2, int(n**0.5)+1):
    if n % i == 0:
        prime_number = False
        break
if prime_number:
    print("소수")
else:
    print("소수 아님")     # 합성수라고도 한다

