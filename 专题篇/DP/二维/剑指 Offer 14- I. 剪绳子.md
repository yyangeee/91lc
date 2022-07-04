# 剑指 Offer 14- I. 剪绳子
https://leetcode-cn.com/problems/jian-sheng-zi-lcof/
## 思路
dp 找出递归公式
https://leetcode-cn.com/problems/jian-sheng-zi-lcof/solution/jian-zhi-offer-14-i-jian-sheng-zi-dong-t-c7ou/## 语法

## 代码
```python
class Solution:
    def cuttingRope(self, n: int) -> int:
        dp = [0] * (n+1)
        dp[2] = 1
        ropemax = 0
        for i in range(2,n+1):
            for j in range(1,i):
                ropemax = max(j * (i-j), j * dp[i-j])
                dp[i] = max(dp[i],ropemax)
        return dp[n]%1000000007 
```
## 复杂度
- 时间复杂度：$O(n)$ 
- 空间复杂度：$O(n)$