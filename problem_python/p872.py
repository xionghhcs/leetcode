# Definition for a binary tree node.

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        def get_sequence(root, seq):
            if root is not None:
                if root.left is None and root.right is None:
                    seq.append(root.val)
                else:
                    get_sequence(root.left, seq)
                    get_sequence(root.right, seq)
        
        s1 = []
        s2 = []
        get_sequence(root1, s1)
        get_sequence(root2, s2)
        if len(s1) != len(s2):
            return False
        else:
            for t1, t2 in zip(s1, s2):
                if t1 != t2:
                    return False
            return True