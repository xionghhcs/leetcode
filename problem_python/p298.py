# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def longestConsecutive(self, root: TreeNode) -> int:
        if root is None:
            return 0
        def get_cnt(root, cnt):
            if root:
                if root.left and root.left.val == root.val + 1:
                    l = get_cnt(root.left, cnt + 1)

                elif root.left is None:
                    l = cnt
                else:
                    l = get_cnt(root.left, 1)
                    l = max(l, cnt)
                if root.right and root.right.val == root.val + 1:
                    r = get_cnt(root.right, cnt + 1)
                elif root.right is None:
                    r = cnt
                else:
                    r = get_cnt(root.right, 1)
                    r = max(r, cnt)
                return max(l, r)
            return cnt

        return get_cnt(root, 1)
