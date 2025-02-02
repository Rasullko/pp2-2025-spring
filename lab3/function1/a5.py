def prmt(s, t, q):
    cnt = 0
    if t == q:
        print(*s)
    else:
        for i in range(t, q + 1):
            s[t], s[i] = s[i], s[t]
            prmt(s, t + 1, q)
            s[t], s[i] = s[i], s[t]
            cnt += 1
    print(cnt)

    

s = input()
s = list(s)
prmt(s, 0, len(s) - 1)