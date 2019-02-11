# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(root):
            if root is None:
                return 0
            else:
                if root.left is not None:
                    l = dfs(root.left)
                else:
                    l = 0
                
                if root.right is not None:
                    r = dfs(root.right)
                else:
                    r = 0
                
                l = l + 1 if root.left is not None and root.left.val == root.val else 0
                r = r + 1 if root.right is not None and root.right.val == root.val else 0

                self.ans = max(self.ans, l + r)
                return max(l, r)
        
        self.ans = 0
        dfs(root)
        return self.ans
            
                