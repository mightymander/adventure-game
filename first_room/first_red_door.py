import time
import random

if wepon_status == 0:
    red_first_desision = input('\nOhh no its a monstor you have no wepon\n\nwould you like to fight with your fists: ')

    if red_first_desision == 'yes':
        exec(open('dead.py').read())

    elif red_first_desision == 'no':
        print('\nyou ran away')
        time.sleep(2)
        exec(open('first_des/ran_away_first_red.py').read())
    
    else:
        print('\nTry again')
    time.sleep(2)
    exec(open('first_room/first_red_door.py').read())

if wepon_status == 1:
    red_first_desision = input('\nOhh no its a monstor \n\nwould you like to fight it: ')  

    if red_first_desision == 'yes':
        win_or_lose = random.choice([0, 1])
        if win_or_lose == 0:
            print('\nYEHHHHH YOU WON')
            time.sleep(2)
            exec(open('first_des/kill_monstor_first.py').read())
    
    if red_first_desision == 'no':
        print('\n okay scardy cat: ')
        exec(open('first_des/got_sword_first_choice.py').read())