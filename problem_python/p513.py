# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        import queue
        q = queue.Queue()
        q.put(root)
        q.put(None)
        ans = root.val
        row = []
        while not q.empty():
            n = q.get()
            if n is None:
                ans = row[0]
                if not q.empty():
                    q.put(None)
                row = []
            else:
                row.append(n.val)
                if n.left is not None:
                    q.put(n.left)
                if n.right is not None:
                    q.put(n.right)
        return ans
    
                