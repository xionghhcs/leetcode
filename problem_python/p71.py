class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        path = path.split('/')
        for p in path:
            if p == '' or p == '.':
                continue
            elif p == '..':
                if len(stack) > 0:
                    stack.pop()
            else:
                stack.append(p)
        if len(stack) == 0:
            return '/'
        else:
            res = []
            for item in stack:
                res.append('/')
                res.append(item)
            return ''.join(res)
                