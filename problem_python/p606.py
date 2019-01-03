class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def tree2str(self, t):
        """
        :type t: TreeNode
        :rtype: str
        """
        def get_ans(t):
            if t is not None:
                cur = t.val
                res = '{}'.format(cur)
                l = get_ans(t.left)
                r = get_ans(t.right)
                if l == '' and r == '':
                    return res
                if l != '' and r == '':
                    res += '({})'.format(l)
                    return res
                if l == '' and r != '':
                    res += '()({})'.format(r)
                    return res
                if l != '' and r != '':
                    res += '({})({})'.format(l, r)
                    return res
                return res
            else:
                return ''
                
        ans = get_ans(t)
        return ans