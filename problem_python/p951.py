# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def flipEquiv(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        if root1 == None or root2 == None:
            return root1 == root2
        
        if root1.val == root2.val:
            return self.flipEquiv(root1.left, root2.right) and self.flipEquiv(root1.right, root2.left) or self.flipEquiv(root1.left, root2.left) and self.flipEquiv(root1.right, root2.right)
        else:
            return False
        