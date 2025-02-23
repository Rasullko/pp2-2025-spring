import re
s = input()
if re.findall("[a-z]+_[a-z]+", s):
    print(True)
else:
    print(False)