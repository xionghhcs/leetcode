# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findLeaves(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []
        
        def dfs(root, ans):
            if root:
                if root.left is not None:
                    if root.left.left is None and root.left.right is None:
                        ans.append(root.left.val)
                        root.left = None
                    else:
                        dfs(root.left, ans)
                if root.right:
                    if root.right.left is None and root.right.right is None:
                        ans.append(root.right.val)
                        root.right = None
                    else:
                        dfs(root.right, ans)
        ans = []
        while root:
            if root.left is None and root.right is None:
                ans.append([root.val])
                break
            else:
                row = []
                dfs(root, row)
                ans.append(row)
        return ans
    