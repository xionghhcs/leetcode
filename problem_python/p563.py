# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def get_sum(root):
            if root is not None:
                return root.val + get_sum(root.left) + get_sum(root.right)
            else:
                return 0 
        

        def get_ans(root):
            if root is not None:
                s_left = get_sum(root.left)
                s_right = get_sum(root.right)
                cur = abs(s_left - s_right)
                left = get_ans(root.left)
                right = get_ans(root.right)
                return cur + left + right
            else:
                return 0
        
        ans = get_ans(root)
        return ans
    