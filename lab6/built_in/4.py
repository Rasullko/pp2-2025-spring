from time import sleep
num, ms = int(input()), int(input())
sleep(ms/1000)
x = pow(num, 0.5)
print(f"Square root of {num} after {ms} miliseconds is {x}")