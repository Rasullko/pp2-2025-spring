import re
s = input()
if re.search("ab{2,3}", s):
    print(True)
else:
    print(False)
