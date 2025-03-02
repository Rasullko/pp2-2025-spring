s = input()
uppercase = 0
lowercase = 0
for i in s:
    if i >= 'a' and i <= 'z':
        lowercase += 1
    if i >= 'A' and i <= 'Z':
        uppercase += 1
print(lowercase, uppercase)