# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# 存在重复元素
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        ans = []
        def preOrder(root, ans):
            if root:
                ans.append(str(root.val))
                preOrder(root.left, ans)
                preOrder(root.right, ans)
            else:
                ans.append('#')
        preOrder(root, ans)
        if len(ans) == 0:
            return ""
        else:
            return ','.join(ans)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        def buildTree(ans, idx):
            if idx[0] >= len(ans):
                return
            if ans[idx[0]] == '#':
                idx[0] += 1
                return None
            val = int(ans[idx[0]])
            idx[0] += 1
            root = TreeNode(val)
            root.left = buildTree(ans, idx)
            root.right = buildTree(ans, idx)
            return root
        
        if data == "":
            return None
        ans = data.split(',')
        idx = [0]
        return buildTree(ans, idx)


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))