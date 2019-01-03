class Solution:
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        def in_order(r, ans):
            if r is not None:
                in_order(r.left, ans)
                ans.append(r.val)
                in_order(r.right, ans)
        ans = []
        in_order(root, ans)
        i = 0
        j = len(ans) - 1
        while i < j:
            if ans[i] + ans[j] == k:
                return True
            if ans[i] + ans[j] < k:
                i += 1
                continue
            
            if ans[i] + ans[j] > k:
                j -= 1
                continue
        return False