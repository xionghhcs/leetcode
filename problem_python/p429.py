
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        ans = []
        import queue
        q = queue.Queue()
        q.put(root)
        while not q.empty():
            tmp_q = queue.Queue()
            tmp_ans = []
            while ! q.empty():
                n = q.get()
                if n is not None:
                    tmp_ans.append(n.val)
                    tmp_q.put(n)
            q = tmp_q
            ans.append(tmp_ans)
        return ans
        