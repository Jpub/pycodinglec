n = int(input("몇 명?: "))
age_sum = 0
i = 1
while i <= n:
    age = int(input("학생 "+str(i)+": "))
    age_sum = age_sum+age
    i = i+1
print("평균: ", age_sum/n)



