# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        def build_tree(nodes):
            if len(nodes) == 0:
                return None
            elif len(nodes) == 1:
                return TreeNode(nodes[0])
            else:
                mid = len(nodes) // 2
                nodes_left = nodes[:mid]
                nodes_right = nodes[mid + 1:]
                node = TreeNode(nodes[mid])
                left_node = build_tree(nodes_left)
                right_node = build_tree(nodes_right )

                node.left = left_node
                node.right = right_node
                return node
       
        root = build_tree(nums)
        return root
