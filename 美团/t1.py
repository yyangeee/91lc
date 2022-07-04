s = input()
a1 = s.count('a')
b1 = s.count('b')
c1 = s.count('c')
cnt = 0
while a1 > 0 and b1 > 0 and c1 > 0:
    if (a1 - 3) >= 0 and (b1-2) >= 0 and (c1-6) >= 0:
        a1 = (a1 - 3)
        b1 = (b1-2)
        c1 = (c1-6)
        cnt += 2
    elif (a1-2) >= 0 and (b1-1) >= 0 and (c1-3) >= 0:
        a1 = (a1 - 2)
        b1 = (b1-1)
        c1 = (c1-3)
        cnt += 1
    else: break
print(cnt)

