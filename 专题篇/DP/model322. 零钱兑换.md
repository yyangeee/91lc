# 322. 零钱兑换
https://leetcode-cn.com/problems/coin-change/
## 思路
dp算法
dp数组i位置对应凑成i所需要硬币个数
## 语法

## 代码
```python
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount+1 for x in range(0,amount+1)]#dp算法通常数列都是目标值+1
        dp[0] = 0
        for i in range(0,len(dp)):
            for coin in coins:
                if i - coin < 0: continue #当i比coin小时，跳出当前的coin循环
                dp[i] = min(dp[i], 1+dp[i-coin]) 
                #不是递归，因为for i 的循环可以从小到大生成
        return -1 if dp[amount] == amount+1 else dp[amount]

```

## 复杂度

- 时间复杂度：$O(n)$
- 空间复杂度：$O(n)$。