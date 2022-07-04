# 剑指 Offer II 031. 最近最少使用缓存
https://leetcode-cn.com/problems/OrIXps/
## 思路
用list记录使用先后
声明一个dict 一个数组。dict记录数值，维护数组最左为最旧值，最右为最新值
get 操作要更新数组
put 要根据list长度判断是否满了，满了的话就remove list。pop(0)位置的值
## 语法
list中去除某值用remove

去除某位置上的数用pop

dict去除某key用pop

只有init的参数用self其他不用
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

