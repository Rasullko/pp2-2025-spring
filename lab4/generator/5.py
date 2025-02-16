n = int(input())
def rev(n):
    for i in range(n, -1, -1):
        yield i
print(*rev(n))