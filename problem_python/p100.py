class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        def equal(p, q):
            if p is None and q is None:
                return True
            elif p is not None and q is not None:
                if p.val == q.val:
                    return equal(p.left, q.left) and equal(p.right, q.right)
                else:
                    return False
            else:
                return False
        return equal(p, q)
        