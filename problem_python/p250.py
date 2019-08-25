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
    
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution2:
    def countUnivalSubtrees(self, root: TreeNode) -> int:
        if root is None:
            return 0
        def dfs(root):
            if root.left is None and root.right is None:
                self.cnt += 1
                return True
            isUnique = True
            if root.left is not None:
                isUnique = dfs(root.left) and isUnique and root.val == root.left.val
            if root.right is not None:
                isUnique = dfs(root.right) and isUnique and root.val == root.right.val
            self.cnt += isUnique
            return isUnique
        self.cnt = 0
        dfs(root)
        return self.cnt