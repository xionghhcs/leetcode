# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        self.ans = -1
        self.pre = None
        self.cnt = 0
        self.res = []
        def in_order(root):
            if root:
                in_order(root.left)
                if self.pre is None:
                    self.pre = root
                    self.cnt = 1
                    self.ans = 1
                    self.res.append(root.val)
                else:
                    if self.pre.val == root.val:
                        self.cnt += 1
                    else:
                        self.cnt = 1
                    if self.cnt == self.ans:
                            self.res.append(root.val)
                    elif self.cnt > self.ans:
                        self.res = [root.val]
                        self.ans = self.cnt
                    
                    self.pre = root
                
                in_order(root.right)
        in_order(root)
        return self.res
    