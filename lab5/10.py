import re
s = input()
t = re.sub(r"([a-z])([A-Z])" , r"\1_\2", s).lower()
print(t)