import os
patha = input()
try:
    os.chdir(patha)
    txta, pathb, txtb = input(), input(), input()
    with open(txta,'r') as infile, open(pathb + "\\" + txtb,'a') as outfile:
        for line in input:
            outfile.write(line)
except Exception as e:
    print(e)