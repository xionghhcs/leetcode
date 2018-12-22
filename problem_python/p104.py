# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def get_max_depth(root, layer):
            if root is None:
                return layer
            else:
                return max(get_max_depth(root.left, layer + 1), get_max_depth(root.right, layer + 1))

        if root is None:
            return 0
        else:
            return get_max_depth(root, 0)