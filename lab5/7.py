import re
s = input()
t = re.sub(r'_',r' ',s).title()
x = t.replace(" ", "")
print(x)