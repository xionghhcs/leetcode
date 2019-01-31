# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        table = dict()
        max_freq = 0
        def get_ans(root):
            if root is not None:
                try:
                    table[root.val] += 1
                    if table[root.val] > max_freq:
                        max_freq = table[root.val]
                except:
                    table[root.val] = 1
                get_ans(root.left)
                get_ans(root.right)
        get_ans(root)
        ans = []
        for k in table:
            if table[k] == max_freq:
                ans.append(k)
        return ans