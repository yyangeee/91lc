# 剑指 Offer 65. 不用加减乘除做加法
https://leetcode-cn.com/problems/bu-yong-jia-jian-cheng-chu-zuo-jia-fa-lcof/
## 思路
https://leetcode-cn.com/problems/bu-yong-jia-jian-cheng-chu-zuo-jia-fa-lcof/solution/mian-shi-ti-65-bu-yong-jia-jian-cheng-chu-zuo-ji-7/
## 语法
1. python存储负数的特性
https://leetcode-cn.com/problems/bu-yong-jia-jian-cheng-chu-zuo-jia-fa-lcof/solution/pythonjie-fa-xiang-xi-jie-du-wei-yun-sua-jrk8/
2. ^异或运算，非进位和
## 代码
```python
1. ^异或运算，非进位和
2. ～取反
class Solution:
    def add(self, a: int, b: int) -> int:
        x = 0xffffffff
        a,b = a & x,b & x
        while b != 0:
            a,b = a^b, (a&b)<<1 & x
        return a if a <= 0x7fffffff else ~(a ^ x)
```
## 复杂度
- 时间复杂度：$O(32)$ 
- 空间复杂度：$O(1)$
  