# 剑指 Offer 60. n个骰子的点数
https://leetcode-cn.com/problems/nge-tou-zi-de-dian-shu-lcof/
## 思路
动态规划
## 代码
```python
class Solution:
    def dicesProbability(self, n: int) -> List[float]:
        dp = [1 / 6] * 6
        for i in range(2, n + 1):
            tmp = [0] * (5 * i + 1)
            for j in range(len(dp)):
                for k in range(6):
                    tmp[j + k] += dp[j] / 6
            dp = tmp
        return dp

```
## 复杂度
- 时间复杂度：$O(n)$ 
- 空间复杂度：$O(n)$