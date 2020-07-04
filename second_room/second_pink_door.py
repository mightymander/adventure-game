import time
import random

win_or_lose = random.choice([1, 2, 3, 4, 5, 6])

lost_dice = random.choice 


print('\nOhh no its a trap you have to roll a 3 to survie')
time.sleep(4)
print('\nRolling')
time.sleep(1)
print('.')
time.sleep(1)
print('.')
time.sleep(1)
print('.')


if win_or_lose == 3:
   print('you won you rolled a 3')
   time.sleep(2)
   exec(open('second_des/second_choice_won.py').read())
else:
    print('\nOhh unlucky you rolled a',win_or_lose,)
    time.sleep(2)
    exec(open('dead.py').read())