import time
import random


first_action = input('\nThe boss throws a rock which way do you jump: ')


def first_action_def():
    if first_action == 'left':
        time.sleep(1)
        exec(open('dead.py').read())

    elif first_action == 'middle':
        time.sleep(1)
        exec(open('dead.py').read())

    elif first_action == 'right':
        time.sleep(1)
        print('\nCongrats you doged it')
        

    else:
        print('try again')
        time.sleep(1)

first_action_def()

time.sleep(2)
second_action = input('\nHe throws another rock quick where do you jump: ')
        
def second_action_def():
    if second_action == 'left':
        time.sleep(1)
        exec(open('dead.py').read())

    elif second_action == 'middle':
        time.sleep(1)
        exec(open('dead.py').read())

    elif second_action == 'right':
        time.sleep(1)
        print('\nwow you won somehow')
        
    else:
        print('try again')
        time.sleep(1)

second_action_def()

print('\nyou only need to survie one more')
time.sleep(2)
print('\nbut the odds are not in your favour')
time.sleep(2)

third_action = input('\nThe main man throws another massive rock left or right???: ')

def third_action_def():
    if third_action == 'left':
        win_or_lose = random.choice([0, 1, 2, 3, 4, 5, 6, 7, 8 ,9])
        if win_or_lose == 0:
            exec(open('win.py').read())
        else:
            exec(open('dead.py').read())

    elif third_action == 'right':
        win_or_lose = random.choice([0, 1, 2, 3, 4, 5, 6, 7, 8 ,9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19])
        if win_or_lose == 0:
            exec(open('win.py').read())
        else:
            exec(open('dead.py').read())

    else:
        print('\nTry again')
        time.sleep(2)
        exec(open('.py').read())
        exec(open('third_des/third_choice_intro.py').read())



third_action_def()
