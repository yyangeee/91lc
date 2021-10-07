#树的普遍定义
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        if not root:
            return []

        queue = [root]

        while queue:
            length = len(queue)  
            in_list = []
            for _ in range(length):
                curnode = queue.pop(0)  # （默认移除列表最后一个元素）这里需要移除队列最头上的那个
                in_list.append(curnode.val)
                if curnode.left: 
                    queue.append(curnode.left)
                if curnode.right: 
                    queue.append(curnode.right)

        return in_list[0]

#建树
a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(3)
d = TreeNode(4)
e = TreeNode(5)
f = TreeNode(6)
g = TreeNode(7)
 
a.left = b
a.right = c
b.left = d
b.right = e
c.left = f
c.right = g


Tra = Solution()
print(Tra.findBottomLeftValue(a))
