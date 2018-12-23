class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def tree2str(self, t):
        """
        :type t: TreeNode
        :rtype: str
        """
        def get_ans(t):
            if t.left is None and t.right is None:
                return '({})'.format(t.val)
            else:
                
        ans = get_ans(t)
        return ans