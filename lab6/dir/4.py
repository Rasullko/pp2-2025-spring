import os
path = input()
try:
    os.chdir(path)
    txt = input()
    try: 
        out = open(txt, 'r')
        cnt = 0
        for line in out:
            if line != "\n": cnt += 1
        print('Number of rows',cnt)
    except Exception as e:
        print(e)   
except Exception as e:
    print(e)