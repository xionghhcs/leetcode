# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        self.ans = root.val
        def inOrder(root):
            if root:
                inOrder(root.left)
                
                if abs(self.ans - target) > abs(root.val - target):
                    self.ans = root.val
                
                inOrder(root.right)
        inOrder(root)
        return self.ans