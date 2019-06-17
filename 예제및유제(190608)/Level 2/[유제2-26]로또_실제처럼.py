from random import choice
from winsound import Beep
from time import sleep
numbers_list = list(range(1, 46))
winning_numbers = []

for n in range(6):
    print(str(n+1)+'번째 숫자를 추첨합니다!')
    sleep(2)
    picked = choice(numbers_list)
    numbers_list.remove(picked)
    winning_numbers.append(picked)
    Beep(1320, 500)
    print(str(winning_numbers[n]))
    print('')
print('마지막, 2등 보너스 번호를 추첨합니다!')
sleep(2)
picked = choice(numbers_list)
numbers_list.remove(picked)
winning_numbers.append(picked)
Beep(1320, 500)
print(str(winning_numbers[6]))
print('')
print('당첨번호는 '+str(winning_numbers[:6])+'입니다.')
print('그리고 2등 보너스 번호는 '+str(winning_numbers[6])+'입니다.')

