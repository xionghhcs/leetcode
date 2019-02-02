# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        target = sum
        self.ans = 0
        def get_sum_from_root(root, s):
            s += root.val
            if s == target:
                self.ans += 1
            if root.left is not None:
                get_sum_from_root(root.left, s)
            if root.right is not None:
                get_sum_from_root(root.right, s)
        
        def get_ans(root):
            if root is not None:
                get_sum_from_root(root, s=0)
                get_ans(root.left)
                get_ans(root.right)
        get_ans(root)
        return self.ans
        

