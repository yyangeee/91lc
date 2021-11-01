# 【Day 53】Top-View-of-a-Tree
https://binarysearch.com/problems/Top-View-of-a-Tree
## 思路
看成一个坐标系
https://leetcode-solution.cn/solutionDetail?type=3&id=53&max_id=2
## 语法
1. sorted(iterable, cmp=None, key=None, reverse=False)
   key为用来进行比较的元素https://www.runoob.com/python/python-func-sorted.html
2. >>> list(map(lambda x: x ** 2, [1, 2, 3, 4, 5]))   # 使用 lambda 匿名函数
   [1, 4, 9, 16, 25]
   list转化为列表https://www.runoob.com/python/python-func-map.html
3. d.items()返回键值对
4. deque双向队列https://www.cnblogs.com/lincappu/p/12890765.html
## 代码
```python
import collections
from typing import Deque
class Solution:
    def solve(self, root):
        tree = collections.deque([(root,0)])
        #deque双端队列，来自collections，支持in 操作，和旋转
        d = {} #字典声明
        while tree:
            cur,pos = tree.popleft()
            if pos not in d:
                d[pos] = cur.val
            if cur.left:
                tree.append((cur.left,pos-1)) #起始点坐标为0，左-右+
            if cur.right:
                tree.append((cur.right,pos+1))
        return list(map(lambda x:x[1], sorted(d.items(), key = lambda x:x[0])))
        #d.items()返回键值对。key = lambda x:x[0] 表示用第一例进行排序即pos
        #map将sorted后的返回值进行x:x[1]函数处理即取val。map(function, iterable, ...)iterable中每一个元素都掉用function
```
## 复杂度

- 时间复杂度：$O(nlogn)$ n个节点，logn为sorted排序的复杂度
- 空间复杂度：$O(n)$

            