import time as tm
from os import system
cls = lambda: system('clear')

fps = 0
time = 0
while time < 100:
    cls()
    tm.sleep(0.1)
    if fps == 0:
        print('\ ')
        fps = 1
    elif fps == 1: 
        print('/ ')
        fps = 2
    elif fps == 2:
        print('- ')
        fps = 0
    time += 1