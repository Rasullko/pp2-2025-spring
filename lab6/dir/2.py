import os
path = input()
try:
    os.chdir(path)
    name = input()
    print("Existence -",     os.access(name, os.F_OK))
    print("Readability -",   os.access(name, os.R_OK))
    print("Writability -",   os.access(name, os.W_OK))
    print("Executability -", os.access(name, os.X_OK))
except Exception as e:
    print(e)