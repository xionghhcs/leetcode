# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def get_depth(root):
            if root is None:
                return 0
            else:
                left = get_depth(root.left)
                right = get_depth(root.right)
                self.ans = max(self.ans, left + right)
                return max(left, right) + 1
        
        self.ans = 0
        get_depth(root)
        return self.ans
    