# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def deleteNode(self, root: 'TreeNode', key: 'int') -> 'TreeNode':
        if root is None:
            return root
        def get_ans(root, key):
            if root.val == key:
                if root.left is None and root.right is None:
                    root = None
                elif root.left is None and root.right is not None:
                    root = root.right
                elif root.left is not None and root.right is None:
                    root = root.left
                else:
                    tmp = root.left
                    root = root.right
                    while root.left is not None:
                        root = root.left
                    root.left = tmp
            else:
                if root.left:
                    get_ans(root.left, key)
                if root.right:
                    get_ans(root.right, key)
                