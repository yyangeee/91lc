# 剑指 Offer II 027. 回文链表
https://leetcode-cn.com/problems/aMhZSa/
## 思路
先找到中点，然后放在队列中进行比较
## 语法
list1.insert(0,slow.val)模拟队列在头部插入
## 代码
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head or not head.next:
            return True

        fast = head
        slow = head
        list1 = []
        while fast and fast.next:
            list1.insert(0,slow.val)
            fast = fast.next.next
            slow = slow.next
        if fast:
            slow = slow.next
            
        for val in list1:
            if val != slow.val:
                return False
            slow = slow.next
        return True

        

```

