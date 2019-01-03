# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def increasingBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        
        def in_order(root, ans):
            if root is not None:
                in_order(root.left, ans)
                ans.append(root.val)
                in_order(root.right, ans)
        
        ans = []
        in_order(root, ans)
        new_head = TreeNode(0)
        rear = new_head
        for v in ans:
            t = TreeNode(v)
            rear.right = t
            rear = t
        return new_head.next
