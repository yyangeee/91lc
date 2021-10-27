# 【Day 47】Number of Operations to Decrement Target to Zero
https://binarysearch.com/problems/Number-of-Operations-to-Decrement-Target-to-Zero
## 思路
题目要求去除数组nums的左右两端元素，并且去除的元素和为target，也就是留下中间的子数组，其和为sum(nums) - target;
题目还要求去除的元素个数越小越好，也就是留下的中间子数组的长度越大越好;
将删除和为target的最小次数，等价于保留若干和为 sum(nums) - target 的数。这样问题就转化为 求连续子数组和为 sum(A) - target 的最长子数组。求连续的数组可以用滑动窗口解决
https://blog.csdn.net/qq_41726606/article/details/114663700
## 语法
## 代码
```python
class Solution:
    def solve(self, nums, target):
        if not nums and not target:
            return 0
        targets = sum(nums) - target
        l = 0
        ans = len(nums)+1  #用于判断是否存在满足题意的答案
        for r in range(len(nums)):
            total += nums[r]
            while l <= r and total > targets:
            # l <= r此条件是根据当nums[1] target = 1的情况
                total -= nums[l]
                l += 1
            if total == targets:
                ans = min(ans, len(nums)-(j-i+1))
        return -1 if ans == len(nums)+1 else ans 
            

```
## 复杂度

- 时间复杂度：$O(n)$
- 空间复杂度：$O(1)$