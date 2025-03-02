import os
path = input()
try:
    os.chdir(path)
    dir = os.listdir(os.getcwd())
    for i in dir:
        if os.path.isdir(i):
            print(f'Directory: {i}')
        elif os.path.isfile(i):
            print(f'File: {i}')
except:
    print('The path does not exist!')