class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def get_ans(r):
            if r :
                get_ans(r.left)
                vals.append(r.val)
                get_ans(r.right)
            return r
        vals = []
        get_ans(root)
        ans = 1000000
        for i in range(1, len(vals)):
            if abs(vals[i-1] - vals[i]) < ans:
                ans = abs(vals[i-1] - vals[i])
        return ans