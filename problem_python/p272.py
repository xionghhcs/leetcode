# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import heapq

class Solution:
    def closestKValues(self, root: TreeNode, target: float, k: int) -> List[int]:
        h = []
        def inOrder(root):
            if root:
                inOrder(root.left)
                
                heapq.heappush(h, [-abs(target - root.val), root.val])
                
                if len(h) > k:
                    heapq.heappop(h)
                
                inOrder(root.right)
        inOrder(root)
        return [t[1] for t in h]
