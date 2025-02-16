print("Enter numbers [a, b):", end=' ')
a, b = list(map(int, input().split()))
def squares():
    for i in range(a, b):
        yield i ** 2
print("Squares of numbers between [a, b):", *squares())