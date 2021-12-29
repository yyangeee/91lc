# 剑指 Offer 04. 二维数组中的查找
https://leetcode-cn.com/problems/er-wei-shu-zu-zhong-de-cha-zhao-lcof/
## 思路
左下角，向上是单调减小，向右是单调增加，所以从左下角便利

## 学到的语法

## 代码
```python
class Solution:
    def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False
        width = len(matrix[0])
        length = len(matrix)
        col = length - 1
        row = 0
        while col >= 0 and row <= width -1:
            if matrix[col][row] == target:
                return True
            elif matrix[col][row] < target:
                row += 1
            else:
                col -= 1
        return False

         

```

## 复杂度

