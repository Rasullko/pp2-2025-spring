import re
s = input()
if re.findall("[A-Z][a-z]+|^[A-Z][a-z]+", s):
    print(True)
else:
    print(False)