# 剑指 Offer II 031. 最近最少使用缓存
https://leetcode-cn.com/problems/OrIXps/
## 思路
用list记录使用先后
## 语法

## 代码
```python
class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.usedlist = []
        self.capacity = capacity


    def get(self, key: int) -> int:
        if key in self.cache:
            if key != self.usedlist[-1]:
                self.usedlist.remove(key)
                self.usedlist.append(key)
            return self.cache[key]
        else: 
            return -1


    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.usedlist.remove(key)
        elif len(self.usedlist) >= self.capacity:
            self.cache.pop(self.usedlist.pop(0))
        self.usedlist.append(key)
        self.cache[key] = value
```

