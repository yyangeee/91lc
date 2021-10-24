# 剑指 Offer 10- I. 斐波那契数列
https://leetcode-cn.com/problems/fei-bo-na-qi-shu-lie-lcof/
## 思路
dp算法
## 语法
取模%
range【）左闭右开
创建长度为n+1 的全0数组 dp = [0 for x in range(0,n+1)]
## 代码
```python
class Solution:
    def fib(self, n: int) -> int:
        if n == 0: return 0
        if n == 1: return 1
 
        MOD = 10 ** 9 + 7
        dp = [0 for x in range(0,n+1)]
        dp[0] = 0 
        dp[1] = 1
        for i in range(2,n+1):
            dp[i] = (dp[i-1] + dp[i-2])%MOD
        return dp[n]
```

## 复杂度

- 时间复杂度：$O(n)$
- 空间复杂度：$O(n)$。