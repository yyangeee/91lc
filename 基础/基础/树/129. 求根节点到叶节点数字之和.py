from collections import deque
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        def dfs(root,cur):
            if not root: return 0
            if not root.left and not root.right: return cur * 10 + root.val
            return dfs(root.left, cur * 10 + root.val) + dfs(root.right, cur * 10 + root.val)
        return dfs(root, 0)

class Solution2:
    def sumNumbers(self, root: TreeNode) -> int:
        res = 0
        q = deque()
        q.append((root,0))
        while q:
            node,value = q.popleft()
            if node.left:
                q.append((node.left,value*10+node.val))
            if node.right:
                q.append((node.right,value*10+node.val))
            if not node.left and not node.right:
                res += value*10+node.val
            print(q)
        return res

#建树
a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(3)
# d = TreeNode(4)
# e = TreeNode(5)
# f = TreeNode(6)
# g = TreeNode(7)
 
a.left = b
a.right = c
# b.left = d
# b.right = e
# c.left = f
# c.right = g


Tra = Solution2()
print(Tra.sumNumbers(a))