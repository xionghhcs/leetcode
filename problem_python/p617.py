class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        if not t1 and t2:
            return t2
        if t1 and not t2:
            return t1
            
        def merge(t1, t2):
            if t1 is not None and t2 is not None:
                t1.val = t1.val + t2.val
                
            elif (t1 and not t2) or (not t1 and not t2):
                return 
            elif not t1 and t2:
                return t2
            
            nc1 = merge(t1.left, t2.left)
            nc2 = merge(t1.right, t2.right)

            if nc1:
                t1.left = nc1

            if nc2:
                t1.right = nc2
                
        merge(t1, t2)
        return t1
                
