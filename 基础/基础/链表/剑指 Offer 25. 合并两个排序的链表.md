# 剑指 Offer 25. 合并两个排序的链表
https://leetcode-cn.com/problems/he-bing-liang-ge-pai-xu-de-lian-biao-lcof/
## 思路
双指针，别忘加入最后剩余的链表
## 语法

## 代码
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        cur = head = ListNode()
        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1               
                l1 = l1.next
            else:
                cur.next = l                
                l2 = l2.next
            cur = cur.next 
        cur.next = l1 if l1 else l2
        return head.next
#递归
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode):
        if not l1: return l2
        if not l2: return l1
        if l1.val < l2.val:
            l1.next = mergeTwoLists(l1.next,l2)
            return l1
        else:
            l2.next = mergeTwoLists(l1,l2.next)
            return l2

```

