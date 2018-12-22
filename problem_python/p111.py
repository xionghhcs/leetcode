# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    min_val = 1e10
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        
        def get_depth(root, layer):
            if root.left is None and root.right is None:
                layer += 1
                print(root.val)
                if layer < self.min_val:
                    self.min_val = layer
                return None
            elif root.left is not None:
                get_depth(root.left, layer + 1)
            elif root.right is not None:
                get_depth(root.right, layer + 1)
        get_depth(root, 0)
        return self.min_val

