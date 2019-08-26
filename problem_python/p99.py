# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def inOrder(root):
            if root:
                inOrder(root.left)
                if self.preNode is not None:
                    if self.firstNode is None and self.preNode.val>= root.val:
                        self.firstNode = self.preNode
                    if self.firstNode and self.preNode.val >= root.val:
                        self.secondNode = root
                self.preNode = root
                inOrder(root.right)
        self.preNode = None
        self.firstNode = None
        self.secondNode = None
        inOrder(root)
        self.firstNode.val, self.secondNode.val = self.secondNode.val, self.firstNode.val
        