# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    

class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        def build_tree(data)
            idx = data.index(max(data)):
            left_data = data[0:idx]

            right_data = data[idx+1:]
            root = TreeNode(data[idx])
            left_node = build_tree(left_data)
            right_node = build_tree(right_data)
            root.left = left_node
            root.right = right_node
            return root
        
        return build_tree(nums)
