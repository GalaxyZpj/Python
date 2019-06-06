from os import system
system('clear')

print(':::Welcome to PI to nth decimal Printer:::\n')
pi = 22/7
choice = True
while choice:
    n = int(input('Enter to how many decimal places the pi value needs to be printed(Upto 51): '))
    print(f'Value of pi: {pi:1.{n}f}')
    c = input('Do you want to quit(y/n): ')
    if c == 'y':
        choice = False
