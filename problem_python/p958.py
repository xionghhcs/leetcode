# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isCompleteTree(self, root: TreeNode) -> bool:
        if root is None:
            return True
        def flag(root, idx):
            if root:
                root.val = idx
                flag(root.left, 2 * idx)
                flag(root.right, 2 * idx + 1)
        flag(root, 1)
        q = [root]
        ans = []
        while len(q) > 0:
            n = q[0]
            del q[0]
            if n:
                ans.append(n.val)
                if n.left:
                    q.append(n.left)
                if n.right:
                    q.append(n.right)
        res = True
        for i in range(1, len(ans)):
            if ans[i] != ans[i-1] + 1:
                res = False
                break
        return res
