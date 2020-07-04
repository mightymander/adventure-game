import time

def intro_text():
    print('\nyou\'ve made it to the end well done')
    time.sleep(4)
    print('\nnow you just have to fight one last boss')
    time.sleep(4)
    print('\nHe\'s kinda op and you prob gonna die hehe')
    time.sleep(4)
    print('\nthe fight is going to work like this')
    time.sleep(4)
    print('\nyou can jump left, right or stay in the middle')
    time.sleep(6)

intro_text()

exec(open('third_des/third_choice.py').read())