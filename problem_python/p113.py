# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        if root is None:
            return []

        self.ans = []
        def get_ans(root, s, path):
            s += root.val
            if root.left is None and root.right is None:
                path.append(root.val)
                if s == sum:
                    self.ans.append(path)
                path.pop()
            else:
                if root.left is not None:
                    path.append(root.val)
                    get_ans(root.left, s, path)
                    path.pop()
                if root.right is not None:
                    path.append(root.val)
                    get_ans(root.right, s, path)
                    path.pop()
        get_ans(root, 0, [])
        return self.ans