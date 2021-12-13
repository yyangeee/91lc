#剑指 Offer II 025. 链表中的两数相加
https://leetcode-cn.com/problems/lMSNwu/
用栈存储，注意进位写法
```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        stack1 = []
        stack2 = []
        stack3 = []
        cur1 = l1
        cur2 = l2
        while cur1:
            stack1.append(cur1.val)
            cur1 = cur1.next
        while cur2:
            stack2.append(cur2.val)
            cur2 = cur2.next
        carry = 0
        while stack1 != None or stack2 != None or carry != 0:
            sum = carry
            sum += stack1.pop() if stack1 else 0
            sum += stack2.pop() if stack2 else 0
            carry = sum // 10
            stack3.append(sum % 10)
        head = ListNode(stack3.pop())
        cur = head

        while stack3:
            cur.next = ListNode(stack3.pop())
            cur = cur.next
        return head

def list2link(List):
    head = ListNode(List[0])#创建一个头节点并将list第一个值赋值给头结点
    p = head#创建头指针
    for i in range(1, len(List)):#list从第二位开始遍历
        p.next = ListNode(List[i])#下一个结点p.next指向list值
        p = p.next#指针往下移动
    return head#返回头结点
l11 = [7,2,4,3]
l22 = [5,6,4]
l1 = list2link(l11)
l2 = list2link(l22)

test = Solution()
print(test.addTwoNumbers(l1,l2))
```