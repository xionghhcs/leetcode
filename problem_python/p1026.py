# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        self.ans = 0
        def dfs(root, max_val, min_val):
            if root:
                max_val = max(root.val, max_val)
                min_val = min(root.val, min_val)
                if root.left is None and root.right is None:
                    self.ans = max(self.ans, abs(max_val - min_val))
                dfs(root.left, max_val, min_val)
                dfs(root.right, max_val, min_val)
        dfs(root, -1, 100000+1)
        return self.ans
      