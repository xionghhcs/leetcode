# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        self.pre = None
        self.root = None
        def in_order(root):
            if root:
                in_order(root.left)
                root.left = None
                if self.pre is None:
                    self.pre = root
                    self.root = root
                else:
                    self.pre.right = root
                    self.pre.left = None
                    self.pre = root
                in_order(root.right)
        in_order(root)
        return self.root