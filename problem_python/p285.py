# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        def inOrder(root):
            if root:
                inOrder(root.right)
                if p == root:
                    self.ans = self.post
                self.post = root
                inOrder(root.left)
        self.post = None
        self.ans = None
        inOrder(root)
        return self.ans
    