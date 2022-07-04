# 剑指 Offer 16. 数值的整数次方
https://leetcode-cn.com/problems/shu-zhi-de-zheng-shu-ci-fang-lcof/
## 思路
二分法
https://leetcode-cn.com/problems/shu-zhi-de-zheng-shu-ci-fang-lcof/solution/jian-dan-li-jie-kuai-su-mi-by-ollieq-rl74/
## 代码
```python
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0:
            return 0
        res = 1
        if n < 0 : x,n = 1/x, -n
        while n:
            if n & 1:
                res *= x
            x *= x
            n >>= 1
        return res


```
## 复杂度
- 时间复杂度：$O(logn)$ 
- 空间复杂度：$O(n)$