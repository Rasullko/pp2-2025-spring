import os
path = input()
try:
    os.chdir(path)
    file = input()
    output = open(file, 'w')
    list = str(list(map(int, input().split())))
    output.write(list)
    output.close()
except Exception as e:
    print(e)