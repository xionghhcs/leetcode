# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isUnivalTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        self.cur = root.val

        def get_ans(root):
            if root is not None:
                if root.val != self.cur:
                    return False
                else:
                    return get_ans(root.left) and get_ans(root.right)
            else:
                return True
        return get_ans(root)