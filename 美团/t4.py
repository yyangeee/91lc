n = int(input())
nums = input().split(' ')
nums = list(map(int, nums))
path = []
res = []
def backtracking(nums,start):
    # 收集子集，要先于终止判断
    res.append(path[:])
    # Base Case
    if start == len(nums):
        return
    # 单层递归逻辑
    for i in range(start,len(nums)):
        path.append(nums[i])
        backtracking(nums,i+1)
        path.pop()
backtracking(nums,0)
total = 0
for i in res:
    length = len(i)
    if 0 < length and length % 2 == 1:
        total += i[length//2]
print(total)