# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def insertIntoBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        def insert(root, val):
            if val < root.val:
                if root.left is None:
                    root.left = TreeNode(val)
                else:
                    insert(root.left, val)
            else:
                if root.right is None:
                    root.right = TreeNode(val)
                else:
                    insert(root.right,val)
        
        insert(root, val)
        return root

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution2:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        node = TreeNode(val)
        if root is None:
            return node
        if val < root.val:
            if root.left is None:
                root.left = node
                return root
            self.insertIntoBST(root.left, val)
            return root
        else:
            if root.right is None:
                root.right = node
                return root
            self.insertIntoBST(root.right, val)
            return root
