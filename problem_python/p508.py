# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def findFrequentTreeSum(self, root: 'TreeNode') -> 'List[int]':
        def get_sum(root):
            if root is not None:
                return root.val + get_sum(root.left) + get_sum(root.right)
            else:
                return 0
        
        def get_ans(root):
            if root is not None:
                s = get_sum(root)
                if s in self.table:
                    self.table[s] += 1
                    if self.max_freq < self.table[s]:
                        self.max_freq = self.table[s]
                else:
                    self.table[s] = 1
                get_ans(root.left)
                get_ans(root.right)
        
        self.max_freq = 1
        self.table = dict()

        get_ans(root)
        ans = []
        for k in self.table:
            if self.table[k] == self.max_freq:
                ans.append(k)
        return ans

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution2:
    cnt = -1
    def findFrequentTreeSum(self, root: TreeNode) -> List[int]:
        table = dict()
        def dfs(root):
            if root:
                l = dfs(root.left)
                r = dfs(root.right)
                cur_s = l + r + root.val
                table[cur_s] = table.get(cur_s, 0) + 1
                self.cnt = max(self.cnt, table.get(cur_s))
                return cur_s
            return 0
        dfs(root)
        ans = []
        for k in table:
            if table[k] == self.cnt:
                ans.append(k)
        return ans
