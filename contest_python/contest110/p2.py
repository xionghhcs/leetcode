# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    ans = 0

    def rangeSumBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: int
        """
        self.look_up(root, L, R)
        return self.ans

    def look_up(self, root, l, r):
        if root is None:
            pass
        else:
            if root.val >= l and root.val <= r:
                self.ans += root.val
            if root.left is not None:
                self.look_up(root.left, l, r)
            if root.right is not None:
                self.look_up(root.right, l, r)
