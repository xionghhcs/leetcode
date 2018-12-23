# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        def search_inner(root, val):
            if root is not None:
                if root.val == val:
                    return root
                else:
                    r1 = search_inner(root.left,val)
                    r2 = search_inner(root.right, val)
                    if r1 != None:
                        return r1
                    if r2 != None:
                        return r2
                    return None
        ans = search_inner(root, val)
        return ans
        
        