# 剑指 Offer II 078. 合并排序链表
https://leetcode-cn.com/problems/vvXgSW/
## 思路
归并排序，二二合并，子问题是合并两个链表
## 语法

## 代码
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists: return None
        
        return self.merge(lists,0,len(lists)-1)
    def merge(self,lists,l: int, r: int):
        # length = len(lists,l: int, r: int)
        # if length <= 1:
        #     return lists
        if l == r:
            return lists[l]
        m = (l + r) // 2
        #mid = length//2
        left = self.merge(lists,l, m)
        right = self.merge(lists, m + 1, r)
        return self.merge_sort(left,right)
    def merge_sort(self,left,right):
        cur1 = left
        cur2 = right
        dummy = head = ListNode()
        while cur1 and cur2:
            if cur1.val < cur2.val:
                head.next = cur1

                cur1 = cur1.next
            else:
                head.next = cur2
                
                cur2 = cur2.next
            head = head.next
        head.next = cur1 if cur1 else cur2
        return dummy.next

        

```

