
from re import A, S


def solution(A, S):
    res = 0
    for i in range(len(A)):
        for j in range(i,len(A)):
            total = sum(A[i:j+1])/(j-i+1)
            if total == S:
                res += 1
    return res
            
    # write your code in Python 3.6
    pass

A = [2,1,3]
S = 2
print(solution(A,S))