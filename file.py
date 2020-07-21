import os
from colorama import Fore, Style

while True:
    path = os.getcwd()
    arr = path.split('/')
    ch = input()
    if ch == 'pwd':
        print(os.getcwd())
    if ch == 'ls':
        for i in os.listdir():
            if i[0] == '.':
                print(Fore.BLUE+i, end=' ')
            elif '.' in i:
                print(Fore.YELLOW+i, end=' ')
            elif '.' not in i:
                print(Fore.GREEN+i, end=' ')
        print(Style.RESET_ALL)
    if 'mkdir' in ch:
        files = ch.split(' ')
        files.pop(0)
        for file in files:
            os.mkdir(file)
    if 'rmdir' in ch:
        files = ch.split(' ')
        files.pop(0)
        for file in files:
            os.rmdir(file)
    elif 'rm' in ch:
        files = ch.split(' ')
        files.pop(0)
        for file in files:
            os.remove(file)
    if ch == 'cd..':
        arr.pop(-1)
        path = ''
        for i in arr:
            path += i + '/'
        os.chdir(path)
    elif 'cd' in ch:
        file = ch.split(' ')
        file.pop(0)
        file = file[0]
        for i in os.listdir(path):
            if file == i:
                os.chdir(i)
    if 'touch' in ch:
        files = ch.split(' ')
        files.pop(0)
        for file in files:
            file = open(file,'x')
            file.close()
    if ch == 'clear':
        print("\n" * 100)
    if 'cat' in ch:
        files = ch.split(' ')
        files.pop(0)
        for file in files:
            file = open(file, 'r')
            print(Fore.CYAN+file.read(), end='')
            file.close()
    if 'nano' in ch:
        file = ch.split(' ')
        file = file[1]
        file = open(file, 'w')
        while True:
            write = input()
            file.write(write)