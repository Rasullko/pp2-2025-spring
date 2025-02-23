import re
s = input()
if re.search("ab*", s):
    print(True)
else:
    print(False)