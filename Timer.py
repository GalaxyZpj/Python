from os import system
from time import sleep
from multiprocessing import pool

system('clear')

def time_up():
    h = 0
    m = 0
    s = 0

    hi, mi, si = input('Enter time(hh:mm:ss): ').split(':')
    hi = int(hi)
    mi = int(mi)
    si = int(si)

    while True:
        system('clear')
        print('\n::::::::::TIMER::::::::::\n')
        print(f'{h}:{m}:{s}')
        if s == 59:
            while True:
                s = 0
                if m == 59:
                    h += 1
                    m = 0
                    while True:
                        s = 0
                        while s < 60:
                            system('clear')
                            print('\n::::::::::TIMER::::::::::\n')
                            print(f'{h}:{m}:{s}')
                            if s == si and m == mi and h == hi:
                                return
                            s += 1
                            sleep(1)
                        m += 1
                m += 1
                while s < 60:
                    system('clear')
                    print('\n::::::::::TIMER::::::::::\n')
                    print(f'{h}:{m}:{s}')
                    if s == si and m == mi:
                        if hi == 0:
                            return
                    s += 1
                    sleep(1)
        if s == si:
            if mi == 0:
                if hi == 0:
                    return
        s += 1
        sleep(1)

def ring():
    while True:
        system('clear')
        print(':::::::::: TIME UP ::::::::::\n\nPlease close the program.\n\n')
        sleep(0.05)
        print(':::::::::: RINGING ::::::::::')
        system("afplay /Users/pranavjain/Github/Python/1.flac")

time_up()
ring()
