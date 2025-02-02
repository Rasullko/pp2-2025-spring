def palin(a):
    b=list(a)
    b.reverse()
    if b==list(a):
        print("Yes")
    else:
        print("No")
a=input()
palin(a)