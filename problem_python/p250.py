# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def countUnivalSubtrees(self, root: TreeNode) -> int:
        
        
        def judge(root, val):
            if root:
                if root.val == val:
                    return judge(root.left, val) and judge(root.right, val)
                else:
                    return False
            else:
                return True
        self.cnt = 0
        def dfs(root):
            if root:
                if judge(root, root.val):
                    self.cnt += 1
                dfs(root.left)
                dfs(root.right)
        dfs(root)
        return self.cnt
    