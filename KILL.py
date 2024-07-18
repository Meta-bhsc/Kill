import os
import time
from colorama import init, Fore, Style

# Initialize colorama
init(autoreset=True)

def clear_screen():
    os.system('clear')

def countdown():
    for i in range(3, 0, -1):
        clear_screen()
        print(Fore.CYAN + f"STARTING in {i}")
        time.sleep(1)
    clear_screen()

def print_boot_up():
    black_lines = [
        '!!!!!           !!!!!     ',
        '!!!!!          !!!!!      ',
        '!!!!!         !!!!!       ',
        '!!!!!        !!!!!        ',
        '!!!!!       !!!!!         ',
        '!!!!!      !!!!!          ',
        '!!!!!     !!!!!           ',
        '!!!!!    !!!!!            ',
        '!!!!!   !!!!!             ',
        '!!!!!    !!!!!            ',
        '!!!!!     !!!!!           ',
        '!!!!!      !!!!!          ',
        '!!!!!       !!!!!         ',
        '!!!!!        !!!!!        ',
        '!!!!!         !!!!!       ',
        '!!!!!          !!!!!      '
    ]
    
    blue_lines = [
        '!!!!!',
        '!!!!!',
        '!!!!!',
        '!!!!!',
        '!!!!!',
        '!!!!!',
        '!!!!!',
        '!!!!!',
        '!!!!!',
        '!!!!!',
        '!!!!!',
        '!!!!!',
        '!!!!!',
        '!!!!!',
        '!!!!!!!!!!!!!!!!!!!!',
        '!!!!!!!!!!!!!!!!!!!!'
    ]
    
    for black, blue in zip(black_lines, blue_lines):
        print(Fore.BLACK + black + Fore.BLUE + blue)
        time.sleep(1)
    
    print(Fore.BLUE + '  ')
    time.sleep(2)
    
    for _ in range(2):
        print(Fore.BLUE + '!!!!!!!!!!!!!!!!!!!!!     ' + Fore.BLACK + '!!!!!')
        time.sleep(1)
    
    for _ in range(10):
        print(Fore.BLUE + '       !!!!!!             ' + Fore.BLACK + '!!!!!')
        time.sleep(1)
    
    for _ in range(2):
        print(Fore.BLUE + '!!!!!!!!!!!!!!!!!!!!!     ' + Fore.BLACK + '!!!!!!!!!!!!!!!!!!!!')
        time.sleep(1)

def main():
    countdown()
    print_boot_up()
    
    print(Fore.YELLOW + 'KILL 1.0 2024 Version')
    time.sleep(1)
    print(Fore.CYAN + 'BY IAN SANDI & CHRIS FARLEY')
    time.sleep(2)
    
    print('')
    print(Fore.LIGHTRED_EX + "1) screen" + " 2)Exit")
    print('')
    time.sleep(1)
    
    try:
        choice = int(input(Fore.CYAN + "What program would you like to run" + Fore.LIGHTRED_EX + "? "))
    except ValueError:
        choice = None
    
    if choice == 1:
        os.system('python3 screen.py')
    elif choice == 2:
        clear_screen()
        time.sleep(1)
        os.system('cd')
        os.system('pwd')
    else:
        print(Fore.CYAN + "Invalid Input")
        time.sleep(1)
        os.system('cd')
        print(Fore.CYAN + "Try Again.")
        time.sleep(1)
        os.system('python3 KILL.py')

if __name__ == "__main__":
    main()
