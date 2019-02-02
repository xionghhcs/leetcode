
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def get_h(root, h):
            if root is None:
                return h
            else:
                if root.left is not None:
                    h_left = get_h(root.left, h+1)
                else:
                    h_left = 0
                
                if root.right is not None:
                    h_right = get_h(root.right, h+1)
                else:
                    h_right = 0
                
                cur_h = max(h_left, h_right)
                return cur_h
        
        def judge(root):
            if root is None:
                return True
            else:
                h_left = get_h(root.left, 0)
                h_right = get_h(root.right, 0)
                if abs(h_left - h_right) >1:
                    return False
                else:
                    return judge(root.left) and judge(root.right)
        
        return judge(root)


