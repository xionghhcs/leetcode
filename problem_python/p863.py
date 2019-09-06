# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root, target, K):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type K: int
        :rtype: List[int]
        """
        def dfs(root, par):
            if root:
                root.par = par
                dfs(root.left, root)
                dfs(root.right, root)
        dfs(root, None)
        
        q = collections.deque([(target, 0)])
        vis = {target}
        while q:
            if q[0][1] == K:
                return [n.val for n, d in q]
            n, d = q.popleft()
            for nn in [n.left, n.right, n.par]:
                if nn and nn not in vis:
                    vis.add(nn)
                    q.append((nn, d+1))
        return []