# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return -1
        self.min = 1000000
        def findSecMin(root):
            if root.left is None:
                return 
            
            if root.val == root.left.val :
                findSecMin(root.left)
            else:
                if root.left.val < self.min:
                    self.min = root.left.val
            
            if root.val == root.right.val:
                findSecMin(root.right)
            else:
                if root.right.val < self.min:
                    self.min = root.right.val
        findSecMin(root)
        if self.min == 1000000:
            return -1
        return self.min