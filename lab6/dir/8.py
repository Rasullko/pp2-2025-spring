import os
path = input()
try:
    os.chdir(path)
    dir = os.listdir(os.getcwd())
    for i in dir:
        if os.path.isdir(i):
            print(f'Direcrotry {i}')
        elif os.path.isfile(i):
            print(f'File {i}')
    file = input()
    os.remove(file)
except Exception as e:
    print(e)