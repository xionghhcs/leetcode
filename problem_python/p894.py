# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    memory = dict()
    def allPossibleFBT(self, N: int) -> List[TreeNode]:
        if N not in self.memory:
            ans = []
            if N == 1:
                ans.append(TreeNode(0))
            elif N % 2 == 1:
                for l in range(0, N):
                    r = N - 1 - l
                    for ll in self.allPossibleFBT(l):
                        for rr in self.allPossibleFBT(r):
                            bst = TreeNode(0)
                            bst.left = ll
                            bst.right = rr
                            ans.append(bst)
            self.memory[N] = ans
        return self.memory[N]
