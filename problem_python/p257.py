# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if root is None:
            return []
        self.ans = []
        def get_path(root, path):
            if root.left is None and root.right is None:
                res = '->'.join([str(item) for item in path])
                self.ans.append(res)
            else:
                if root.left is not None:
                    path.append(root.left.val)
                    get_path(root.left, path)
                    path.pop()
                if root.right is not None:
                    path.append(root.right.val)
                    get_path(root.right, path)
                    path.pop()
        path = [root.val]
        get_path(root, path)
        return self.ans