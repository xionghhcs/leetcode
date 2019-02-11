# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def smallestFromLeaf(self, root: 'TreeNode') -> 'str':
        ans = 'z' * 1000
        def get_ans(root, s):
            if root.left is None and root.right is None:
                nonlocal ans
                if chr(root.val + 97) + s < ans:
                    ans = chr(root.val + 97) + s
            
            if root.left:
                get_ans(root.left, chr(root.val + 97) + s)
            if root.right:
                get_ans(root.right,, chr(root.val + 97) + s)
        
        get_ans(root, '')

        return ans
