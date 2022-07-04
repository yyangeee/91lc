# 剑指 Offer 46. 把数字翻译成字符串
https://leetcode-cn.com/problems/ba-shu-zi-fan-yi-cheng-zi-fu-chuan-lcof/
## 思路
dp 或者递归
https://leetcode-cn.com/problems/ba-shu-zi-fan-yi-cheng-zi-fu-chuan-lcof/solution/mian-shi-ti-46-ba-shu-zi-fan-yi-cheng-zi-fu-chua-6/
https://leetcode-cn.com/problems/ba-shu-zi-fan-yi-cheng-zi-fu-chuan-lcof/solution/dong-tai-gui-hua-dp-by-z1m/
## 学到的语法


## 代码
```py
class Solution:
    def translateNum(self, num: int) -> int:
        def dfs(s,idx):
            n = len(s)
            if idx == n: return 1
            if idx == n-1 or s[idx] == '0' or s[idx:idx+2] > '25':
                return dfs(s,idx+1)
            else:
                return dfs(s,idx+1) + dfs(s,idx+2)
        s = str(num)
        return dfs(s,0)


class Solution:
    def translateNum(self, num: int) -> int:
        s = str(num)
        n = len(s)
        dp = [1 for _ in range(n+1)] 
        for i in range(2,n+1):
            if '10' <= s[i-2:i] < '26':
                dp[i] = dp[i - 2] + dp[i - 1]
            else:
                dp[i] = dp[i - 1]
        return dp[n]

```

## 复杂度


