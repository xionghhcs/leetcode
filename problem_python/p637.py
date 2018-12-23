# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        import queue
        q = queue.Queue()
        q.put(root)
        ans = []
        while not q.empty():
            tmp_q = queue.Queue()
            tmp_ans = []
            while not q.empty():
                n = q.get()
                if n is not None:
                    tmp_ans.append(n.val)
                    if n.left is not None:
                        tmp_q.put(n.left)
                    if n.right is not None:
                        tmp_q.put(n.right)
            ans.append(sum(tmp_ans) / len(tmp_ans))
            q = tmp_q
        return ans