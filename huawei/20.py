class Solution:
    def isValid(self, s: str) -> bool:
        if s is None:
            return False
        if s == '':
            return True
        stack = []
        table = {}
        table['(']=')'
        table['[']=']'
        table['{']='}'

        for c in s:
            if c in ['(','[','{']:
                stack.append(c)
            else:
                if len(stack)>0:
                    tmp = stack[-1]
                    if table[tmp] == c:
                        del stack[-1]
                    else:
                        return False
                else:
                    return False
        return len(stack) == 0



