# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def constructFromPrePost(self, pre: List[int], post: List[int]) -> TreeNode:
        if len(pre) == 0:
          return None
        if len(pre) == 1:
          return TreeNode(pre[0])
        root = TreeNode(pre[0])
        left_root = pre[1]
        idx = post.index(left_root) + 1
        l = self.constructFromPrePost(pre[1:1+idx], post[:idx])
        r = self.constructFromPrePost(pre[1+idx:], post[idx:len(post)-1])
        root.left = l
        root.right = r
        return root
