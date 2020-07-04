import time

first_action = input("\nThere are 3 doors a red one, blue one and a green one \n\nwhich one do you choose: ")

if first_action == 'red':
    print('\nalready killed that dude')
    time.sleep(2)
    exec(open('first_des/kill_monstor_first.py').read())

elif first_action == 'blue':
     print('\nalready got sword')
     time.sleep(2)
     exec(open('first_des/got_sword_also_run_away.py').read())

elif first_action == 'green':
     print('you picked green')  
     exec(open('first_room/first_green_door.py').read())

else:
    print('\nTry again')
    time.sleep(2)
    exec(open('first_des/first_choice.py').read())

import time

