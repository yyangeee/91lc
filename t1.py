s = input()
s1 = s[2:-2].split(',')
s2 = input()
s2 = s2[1:-2].split(',')
s3 = input()
s3 = s3[1:-2].split(',')
s4 = input()
s4 = s4[1:-2].split(',')
s5 = input()
s5 = s5[1:-2].split(',')

arr = []
arr.append(s1[:])
arr.append(s2[:])
arr.append(s3[:])
arr.append(s4[:])
arr.append(s5[:])
def dfs(arr, i, j):
    if not 0 <= i < len(arr) or not 0 <= j < len(arr[0]) or arr[i][j] == '0': return
    arr[i][j] = '0'
    dfs(arr, i + 1, j)
    dfs(arr, i, j + 1)
    dfs(arr, i - 1, j)
    dfs(arr, i, j - 1)
count = 0
for i in range(len(arr)):
    for j in range(len(arr[0])):
        if arr[i][j] == '1':
            dfs(arr, i, j)
            count += 1
print(count)
