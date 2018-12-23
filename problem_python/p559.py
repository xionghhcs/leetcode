
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        if root is None:
            return 0
        def get_depth(root, layer):
            if root is not None:
                max_val = 0
                for n in root.children:
                    c_d = get_depth(n, layer + 1)
                    max_val = max(max_val, c_d)
                max_val = max(layer, max_val)
                return max_val
        
        ans = get_depth(root, 1)
        return ans
        