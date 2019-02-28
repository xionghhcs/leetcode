# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        if root is None or k == 0:
            return None
        def in_order(node, k):
            if node is not None:
                ans = None
                ans = in_order(node.left, k)
                if ans is None:
                    if k[0] == 1:
                        ans = node.val
                    k[0] -= 1
                
                if ans is None:
                    ans = in_order(node.right, k)
                return ans
            return None


        