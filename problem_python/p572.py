# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        def judge(s, t):
            if s is None and t is not None:
                return False
            if s is not None and t is None:
                return False
            if s is None and t is None:
                return True
            if s.val == t.val:
                return judge(s.left, t.left) and judge(s.right, t.right)
            else:
                return False
        self.ans = False
        def get_ans(s, t):
            r = judge(s, t)
            if r is True:
                self.ans = True
            if s is None:
                return 
            get_ans(s.left, t)
            get_ans(s.right, t)
        
        get_ans(s, t)
        return self.ans