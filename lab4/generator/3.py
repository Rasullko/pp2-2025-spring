def div_3_4():
    for i in range(int(input())):
        if (i % 3 == 0 and i % 4 == 0):
            yield i
print(*div_3_4())
