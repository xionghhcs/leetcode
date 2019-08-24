"""
# Definition for a Node.
class Node:
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if root is None:
            return None
        def inOrder(root):
            nonlocal first, last
            if root:
                inOrder(root.left)
                
                if last:
                    last.right = root
                    root.left = last
                else:
                    first = root
                last = root
                
                inOrder(root.right)
        
        first, last = None, None
        inOrder(root)
        last.right = first
        first.left = last
        return first
