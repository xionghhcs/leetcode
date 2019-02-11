# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def deleteNode(self, root: 'TreeNode', key: 'int') -> 'TreeNode':
        if root is None:
            return None
        if root.val == key:
            if root.left is None and root.right is None:
                return None
            elif root.left is not None and root.right is None:
                return root.left
            elif root.left is None and root.right is not None:
                return root.right
            else:
                tmp = root.left
                root = root.right
                cur = root
                while cur.left is not None:
                    cur = cur.left
                cur.left = tmp
                return root
        
        root.left = self.deleteNode(root.left, key)
        root.right = self.deleteNode(root.right, key)
        return root

        


                