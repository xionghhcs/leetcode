class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def equal(p, q):
            if p is None and q is None:
                return True
            elif p is not None and q is not None:
                if p.val == q.val:
                    return equal(p.left, q.right) and equal(p.right, q.left)
                else:
                    return False
            else:
                return False
        if root is None:
            return True
        else:
            return  equal(root.left, root.right)