
nums = "abcbcbcabc"
path = []
res = []
mapp = dict()
def backtracking(nums,start):
    # 收集子集，要先于终止判断
    subnum = "".join(path)
    mapp[subnum] = mapp.setdefault(subnum,0) + 1
    # Base Case
    if start == len(nums):
        return
    # 单层递归逻辑
    for i in range(start,len(nums)):
        path.append(nums[i])
        backtracking(nums,i+1)
        path.pop()
backtracking(nums,0)
a = sorted(mapp.items(), key=lambda x: x[1], reverse=True)
print(a[0][1])
