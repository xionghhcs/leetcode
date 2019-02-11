# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        def pre_order(root, ans):
            if root is not None:
                ans.append(root.val)
                pre_order(root.left, ans)
                pre_order(root.right, ans)
        
        ans = []
        pre_order(root)
        return ans
    