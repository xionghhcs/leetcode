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

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution2:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if root is None:
            return None
        if root.val == key:
            if root.left is not None:
                find = root.left
                while find.right is not None:
                    find = find.right
                find.right = root.right
                return root.left
            elif root.right is not None:
                find = root.right
                while find.left is not None:
                    find = find.left
                find.left = root.left
                return root.right
            return None
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
            return root
        else:
            root.left = self.deleteNode(root.left, key)
            return root
        