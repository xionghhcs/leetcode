class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        def judge(root, path_sum):
            if root.left is None and root.right is None:
                path_sum += root.val
                if path_sum == sum:
                    return True
                else:
                    return False
            else:
                if root.left is not None and root.right is not None:
                    return judge(root.left, path_sum + root.val) or judge(root.right, path_sum + root.val)
                elif root.left is not None and root.right is None:
                    return judge(root.left, path_sum + root.val)
                elif root.left is None and root.right is not None:
                    return judge(root.right, path_sum + root.val)
        if root is None:
            return False
        else:
            return judge(root, 0)
        