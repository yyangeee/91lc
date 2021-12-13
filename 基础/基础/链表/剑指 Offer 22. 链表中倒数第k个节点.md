# 剑指 Offer 22. 链表中倒数第k个节点
https://leetcode-cn.com/problems/lian-biao-zhong-dao-shu-di-kge-jie-dian-lcof/
## 思路
快慢指针，两者距离为k
## 语法

## 代码
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        fast,slow = head,head
        while k:
            fast,k = fast.next, k-1
        while fast:
            slow , fast = slow.next , fast.next
        return slow
```