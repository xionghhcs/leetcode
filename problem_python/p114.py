# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if root is None:
            return None
        flatten(root.left)
        flatten(root.right)
        tmp = root.right
        root.right = root.left
        root.left = None
        while root.right is not None:
            root = root.right
        root.right = tmp
