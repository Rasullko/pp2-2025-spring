import math
N = int(input("Number of sides: "))
L = int(input("Length of side: "))
P = N * L
x = int(math.tan(180/N))
a = L/(2*x)
A = (P * a)/2
print("Area is: ", A)