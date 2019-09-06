# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def str2tree(self, s: str) -> TreeNode:
        if s=="":
            return None
        
        def dfs(sub):
            if len(sub) == 0:
                return None
            idx = 0
            while idx < len(sub) and sub[idx] != '(':
                idx += 1
            val = int(sub[:idx])
            root = TreeNode(val)
            l = 1
            i = idx + 1
            while i < len(sub):
                if sub[i] == '(':
                    l += 1
                elif sub[i] == ')':
                    l -= 1
                if l == 0:
                    break
                i += 1
            s1 = sub[idx+1:i]
            s2 = sub[i+2:-1]
            root.left = dfs(s1)
            root.right = dfs(s2)
            return root
        return dfs(s)
