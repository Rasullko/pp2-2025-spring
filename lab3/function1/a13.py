import random

name = input("Hello! What is your name? \n")
print()

print(f"Well, {name}, I am thinking of a number between 1 and 20.")
rndm = random.randint(1,20)
n = int(input("Take a guess.\n"))
cnt = 1
while n != rndm:
    if n > rndm:
        print("Your guess is too high.")
    elif n < rndm:
        print("Your guess is too low,")
    cnt += 1
    n = int(input("Take a guess.\n"))

print(f"Good job, {name}! You guessed my number in {cnt} guesses")