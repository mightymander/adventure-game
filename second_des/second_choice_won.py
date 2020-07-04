import time

second_action = input("\nThere are 2 doors a pink one and a white one \n\nwhich one do you choose: ")

if second_action == 'pink':
    print('\ncant pick pink already won')
    time.sleep(2)
    exec(open('second_des/second_choice_won.py').read())

elif second_action == 'white':
     print('you picked white')  
     exec(open('second_room/second_white_door.py').read())
     
else:
    print('\nTry again')
    time.sleep(2)
    exec(open('main.py').read())