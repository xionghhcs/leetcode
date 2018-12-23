class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        def reverse(root):
            if reverse is not None:
                tmp = root.left
                root.left = root.right
                root.right = tmp

                reverse(root.left)
                reverse(root.right)
        reverse(root)
        return root