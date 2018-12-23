# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def minDiffInBST(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.ans = []
        def get_ans(root):
            if root is not None:
                self.ans.append(root.val)
                get_ans(root.left)
                get_ans(root.right)
        get_ans(root)
        self.ans.sort()
        res = 1e10
        for i in range(1, len(self.ans)):
            dist = abs(self.ans[i] - self.ans[i-1])
            res = dist if dist < res else res
        return res