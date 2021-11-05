# 剑指 Offer 56 - I. 数组中数字出现的次数
https://leetcode-cn.com/problems/shu-zu-zhong-shu-zi-chu-xian-de-ci-shu-lcof/
## 思路
相同的数做异或^,结果为0
https://leetcode-cn.com/problems/shu-zu-zhong-shu-zi-chu-xian-de-ci-shu-lcof/solution/zhi-chu-xian-yi-ci-de-shu-xi-lie-wei-yun-suan-by-a/
## 语法
## 代码
```python
class Solution:
    def singleNumbers(self, nums):
        test = 0
        a,b = 0,0
        for num in nums:
            test ^= num
        h = 1
        while test & h == 0:
            h <<= 1 #找到最右侧的1位
        for num in nums:
            if num & h == 0:
                a ^= num
            else:    #不能写成 if num & h == 1: 因为异或运算后为1的位置不一定是最后一位，可能是2/4/8.。。。
                b ^= num 
        return a,b
dd = Solution()
str = [1,2,5,2]
print(dd.singleNumbers(str))
```
## 复杂度
- 时间复杂度：$O(n)$ 
- 空间复杂度：$O(1)$