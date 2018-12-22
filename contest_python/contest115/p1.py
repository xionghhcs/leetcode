# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

import queue


class Solution:
    def isCompleteTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return False
        q = queue.Queue()
        q.put(root)
        res = []
        while not q.empty():
            node = q.get()
            res.append(node)
            if node is None:
                continue
            q.put(node.left)
            q.put(node.right)

        for idx, n in enumerate(res, start=1):
            if n is None:
                for n in res[idx:]:
                    if n is not None:
                        return False
        return True

