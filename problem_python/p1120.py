# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maximumAverageSubtree(self, root: TreeNode) -> float:
        if root is None:
            return 0
        
        self.ans = 0
        def postOrder(root):
            l = [0,0]
            r = [0,0]
            if root.left:
                l = postOrder(root.left)
            if root.right:
                r = postOrder(root.right)
            cur_s = l[0] + r[0] + root.val
            cnt = r[1] + l[1] + 1
            self.ans = max(self.ans, cur_s / cnt)
            return [cur_s, cnt]
        postOrder(root)
        return self.ans
    
            
            