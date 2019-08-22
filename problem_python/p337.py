# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rob(self, root: TreeNode) -> int:
        def dfs(root):
          if root is None:
            return [0,0]
          l = dfs(root.left)
          r = dfs(root.right)
          
          return [max(l) + max(r),root.val + l[0] + r[0]]
          
        res = dfs(root)
        return max(res)
