# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrder(self, root: 'TreeNode') -> 'List[List[int]]':
        if root is None:
            return []

        import queue
        import copy
        q = queue.Queue()
        q.put(root)
        q.put(None)
        row = []
        ans = []
        while not q.empty():
            n = q.get()
            if n is None:
                ans.append(row)
                row = []
                if not q.empty():
                    q.put(None)
            else:
                row.append(n.val)
                if n.left:
                    q.put(n.left)
                if n.right:
                    q.put(n.right)
        return ans
