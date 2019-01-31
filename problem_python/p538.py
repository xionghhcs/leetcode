# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        def in_order(root):
            if root is not None:
                in_order(root.left)
                vals.append(root.val)
                in_order(root.right)
        
        vals = []
        in_order(root)
        self.sum = 0
        def in_order_2(root):
            if root is not None:
                in_order_2(root.right)
                self.sum += vals.pop()
                root.val = self.sum
                in_order_2(root.left)
        in_order_2(root)
        return root