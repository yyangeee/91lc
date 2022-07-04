# 剑指 Offer 49. 丑数
https://leetcode-cn.com/problems/chou-shu-lcof/
## 思路
动态规划
## 代码
```python
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        dp = [0] * n
        dp[0] = 1
        a,b,c = 0,0,0
        for i in range(1,n):
            num2 = dp[a] * 2
            num3 = dp[b] * 3
            num5 = dp[c] * 5
            dp[i] = min(num2,num3,num5)
            if dp[i] == num2:
                a += 1
            if dp[i] == num3:
                b += 1
            if dp[i] == num5:
                c += 1
        return dp[n-1]

```
## 复杂度
- 时间复杂度：$O(n)$ 
- 空间复杂度：$O(n)$