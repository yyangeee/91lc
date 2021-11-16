# -*- coding:utf-8 -*-

'二叉树结点类'


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


'列表创建二叉树'


def listCreatTree(root, llist, i):
    if i < len(llist):
        if llist[i] == '#':
            return None  ###这里的return很重要
        else:
            root = TreeNode(llist[i])
            # 往左递推
            root.left = listCreatTree(root.left, llist, 2 * i + 1)  # 从根开始一直到最左，直至为空，
            # 往右回溯
            root.right = listCreatTree(root.right, llist, 2 * i + 2)  # 再返回上一个根，回溯右，
            # 再返回根'
            return root  ###这里的return很重要
    return root


# 先序遍历二叉树
def preOrderBT(root):
    if not root:
        return None
    print(root.val, end='\t')
    preOrderBT(root.left)
    preOrderBT(root.right)


# 中序遍历二叉树
def midOrdBT(root):
    if not root:
        return "#"
    midOrdBT(root.left)
    print(root.val, end="\t")
    midOrdBT(root.right)


if __name__ == '__main__':
    #llist = ['1', '2', '3', '#', '4', '5', '6']  #层序遍历的树，空节点用#表示
    llist = input().split(',')
    l1list = input().split(',')

    root = listCreatTree(None, llist, 0)
    #p = root
    print(".............................")
    preOrderBT(root)
    print()
    midOrdBT(root)
    print(root.val)
    while root




class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        sorted = []
        p1, p2 = 0, 0
        while p1 < m or p2 < n:
            if p1 == m:
                sorted.append(nums2[p2])
                p2 += 1
            elif p2 == n:
                sorted.append(nums1[p1])
                p1 += 1
            elif nums1[p1] < nums2[p2]:
                sorted.append(nums1[p1])
                p1 += 1
            else:
                sorted.append(nums2[p2])
                p2 += 1
        nums1[:] = sorted

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/merge-sorted-array/solution/he-bing-liang-ge-you-xu-shu-zu-by-leetco-rrb0/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

