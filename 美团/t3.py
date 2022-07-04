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
result = 0
for i in res:
    total= sum(i)
    if total % 7 == 0:
        result = max(result,total)
print(result)