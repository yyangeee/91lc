class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        def dfs(cur):
            if not cur: return 
            dfs(cur.left)
            if self.pre:
                self.pre.right = cur
                cur.left = self.pre
            else:
                self.head = cur
            self.pre = cur
            dfs(cur.right)


        if not root: return None
        self.pre = None
        dfs(root)
        self.head.left ,self.pre.right = self.pre, self.head
        return self.head

