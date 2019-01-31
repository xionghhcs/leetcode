class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        self.ans = 0
        def get_ans(root):
            if root is not None:
                if root.left is not None and root.left.left is None and root.left.right is None:
                    self.ans += root.left.val
                get_ans(root.left)
                get_ans(root.right)
        get_ans(root)
        return self.ans