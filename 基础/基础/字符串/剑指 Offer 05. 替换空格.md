# 剑指 Offer 05. 替换空格
https://leetcode-cn.com/problems/ti-huan-kong-ge-lcof/
## 思路

## 语法
''.join(res)
## 代码
```python
class Solution:
    def replaceSpace(self, s: str) -> str:
        res = []
        for i in s:
            if i == ' ':
                res.append('%20')
            else:
                res.append(i)
        return ''.join(res)

```

