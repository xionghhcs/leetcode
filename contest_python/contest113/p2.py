# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def flipEquiv(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """

        return False

    def check(self, r1, r2):
        if r1.val == r2.val:
            if r1.left == r2.left and r1.right == r2.right:
                return self.check(r1.left, r2.left) and self.check(r1.right, r2.right)
            elif r1.left == r2.left and r1.right != r2.right:
                return False
            elif r1.left != r2.left and r1.right == r2.right:
                return False
            elif r1.left != r2.left and r1.right != r2.right:
                pass
            pass
        else:
            pass