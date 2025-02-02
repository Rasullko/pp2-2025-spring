def solve(numheads, numlegs):
    arr = []
    for rheads in range(numheads + 1):
        chheads = numheads - rheads
        if (((chheads * 2) + (rheads * 4)) == numlegs):
            arr.append(rheads)
            arr.append(chheads)
    return arr

n = list(map(int, input().split()))
print(*solve(n[0], n[1]))