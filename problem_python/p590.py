
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children

class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        def preorder_inner(root, ans):
            if root is not None:
                for n in root.children:
                    preorder_inner(n, ans)
                ans.append(root.val)
        ans = []
        preorder_inner(root, ans)
        return ans
        