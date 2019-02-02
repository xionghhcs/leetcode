# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        def in_order(root, res):
            if root is not None:
                in_order(root.left, res)
                res.append(root.val)
                in_order(root.right, res)
        
        res = []
        in_order(root, res)
        return res