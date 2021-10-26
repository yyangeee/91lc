# 二分法
## 二分查找思路
1.循环体内，我们不断计算 mid ，并将 nums[mid] 与 目标值比对。
 
2.如果 nums[mid] 等于目标值， 则提前返回 mid（只需要找到一个满足条件的即可）

3.如果 nums[mid] 小于目标值， 说明目标值在 mid 右侧，这个时候搜索区间可缩小为 [mid + 1, right] （mid 以及 mid 左侧的数字被我们排除在外）

4.如果 nums[mid] 大于目标值， 说明目标值在 mid 左侧，这个时候搜索区间可缩小为 [left, mid - 1] （mid 以及 mid 右侧的数字被我们排除在外）

循环结束都没有找到，则说明找不到，返回 -1 表示未找到。
## 代码
```python
def binarySearch(nums, target):
    # 左右都闭合的区间 [l, r]
    l, r = 0, len(nums) - 1
    while l <= r:
        mid = (left + right) >> 1 
        #右移运算符>>,运算结果正好能对应一个整数的二分之一值，这就正好能代替数学上的除2运算，但是比除2运算要快。
        if nums[mid] == target: return mid
        # 搜索区间变为 [mid+1, right]
        if nums[mid] < target: l = mid + 1
        # 搜索区间变为 [left, mid - 1]
        if nums[mid] > target: r = mid - 1
    return -1
```


## 复杂度

- 时间复杂度：$O(n)$
- 空间复杂度：$O(n)$。