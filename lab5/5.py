import re
s = input()
if re.findall("a.*b", s):
    print(True)
else:
    print(False)