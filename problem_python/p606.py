# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def tree2str(self, t: TreeNode) -> str:
        self.ans = []
        def preorder(root):
            if root is not None:
                if root.left is None and root.right is None:
                    return '{}'.format(root.val)
                if root.left is None and root.right is not None:
                    return '{}()({})'.format(root.val, preorder(root.right))
                if root.left is not None and root.right is None:
                    return '{}({})'.format(root.val, preorder(root.left))
                return '{}({})({})'.format(root.val, preorder(root.left), preorder(root.right))
            else:
                return ""
        res = preorder(t)
        return res