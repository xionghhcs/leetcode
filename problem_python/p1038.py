# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        self.post = 0
        def inOrder(root):
            if root:
                inOrder(root.right)
                
                cur_s = self.post + root.val
                root.val = cur_s
                self.post = cur_s
                
                inOrder(root.left)
        inOrder(root)
        return root
    