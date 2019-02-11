# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def largestValues(self, root: 'TreeNode') -> 'List[int]':
        if root is None:
            return []
        
        import queue
        q = queue.Queue()
        q.put(root)
        ans = []
        row = []
        while not q.empty():
            n = q.get()
            if n is None:
                ans.append(max(row))
                row = []
                if not q.empty():
                    q.put(None)
            else:
                row.append(n.val)
                if n.left is not None:
                    q.put(n.left)
                
                if n.right is not None:
                    q.put(n.right)
        return ans
    