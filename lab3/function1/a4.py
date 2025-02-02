def filter_prime(n):
    res = []
    for i in range(len(n)):
        prime = True
        if int(n[i])<2:
            continue
        for j in range(2, int(n[i]) // 2 + 1):
            if(int(n[i]) % j == 0):
                prime = False
                break
       
        if(prime):
            res.append(int(n[i]))
    return res

x = input().split()
print(*filter_prime(x))