import re
s = input()
t = re.sub("[ ,.]", ":", s)
print(t)