# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        def postOrder(root):
            if root:
                ln, l = postOrder(root.left)
                rn, r = postOrder(root.right)
                if l < r:
                    return rn, r + 1
                elif l > r:
                    return ln, l + 1
                else:
                    return root, l + 1
            else:
                return None, 0
        ans, _ = postOrder(root)
        return ans
    