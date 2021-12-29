# 剑指 Offer 58 - II. 左旋转字符串
https://leetcode-cn.com/problems/zuo-xuan-zhuan-zi-fu-chuan-lcof/
## 思路

## 语法
''.join(res)
## 代码
```python
class Solution:
    def reverseLeftWords(self, s: str, n: int) -> str:
        if not s:
            return []
        text = list(s)
        res = []
        return "".join(text[n:]) + "".join(text[0:n])

```

