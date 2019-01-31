# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        import copy
        ans = []
        def get_path(root, path, target):
            if root.val == target:
                path.append(root.val)
                ans.append(copy.deepcopy(path))
            else:
                path.append(root.val)
                if root.left is not None:
                    get_path(root.left, path, target)
                    path.pop()
                if root.right is not None:
                    get_path(root.right, path, target)
                    path.pop()
    
        get_path(root, [], p.val)
        get_path(root, [], q.val)
        res = None
        for i1, i2 in zip(ans[0], ans[1]):
            if i1 == i2:
                res = i1
        return res

                