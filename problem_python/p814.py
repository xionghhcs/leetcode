
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def pruneTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root is None:
            return None
        
        if root.val == 0 and root.left is None and root.right is None:
            return None
        
        def has_one(root):
            if root.val == 1:
                return True
            else:
                if root.left is not None:
                    l = has_one(root.left)
                else:
                    l = False
                
                if root.right is not None:
                    r = has_one(root.right)
                else:
                    r = False
                
                return l or r
            
        def get_ans(root):
            if root.left is not None:
                l = has_one(root.left)
                if l is True:
                    get_ans(root.left)
                else:
                    root.left = None
            
            if root.right is not None:
                r = has_one(root.right)
                if r is True:
                    get_ans(root.right)
                else:
                    root.right = None
        
        get_ans(root)
        
        return root
