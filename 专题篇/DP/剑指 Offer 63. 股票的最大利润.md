# 剑指 Offer 63. 股票的最大利润
https://leetcode-cn.com/problems/gu-piao-de-zui-da-li-run-lcof/
## 思路
遍历一次 minval存目前的最小值
maxval 存当前最大值 不断更新
## 代码
```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int: 
        if len(prices) ==0:
            return 0
        minval = prices[0]
        maxval = 0
        for i in range(0,len(prices)):
            if prices[i] <= minval:
                minval = prices[i]
            else:
                maxval = max((prices[i]-minval),maxval)
        return maxval

```
## 复杂度
- 时间复杂度：$O(n)$ 
- 空间复杂度：$O(n)$