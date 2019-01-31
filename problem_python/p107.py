class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        ans = []
        from queue import Queue
        q = Queue()
        q.put(root)
        q.put(None)

        level = []
        while not q.empty():
            n = q.get()
            if n is None:
                ans.append(level)
                level = []
                if not q.empty():
                    q.put(None)
            else:
                if n.left is not None:
                    q.put(n.left)
                if n.right is not None:
                    q.put(n.right)
        return ans[::-1]
        
        