# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def postorderTraversal(self, root: 'TreeNode') -> 'List[int]':
        ans = []
        s = []
        s.append(root)
        while len(s) > 0:
            n = s.pop()
            if n is not None:
                ans.append(n.val)
                s.append(n.left)
                s.append(n.right)
        return ans[::-1]
    