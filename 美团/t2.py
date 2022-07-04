n = int(input())
s = input().split(' ')
s = list(map(int, s))
res = s[-1]
if len(s) == 2:
    print(s[-1] - s[0])
else:

    for i in range(1,len(s)-1):
        tmp = (s[-1]-s[i])-(s[i] -s[0])
        res = min(res,tmp)
    print(res)
