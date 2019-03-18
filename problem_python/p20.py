class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        table = {}
        table[')'] = '('
        table[']'] = '['
        table['}'] = '{'
        for idx, c in enumerate(s):
            if c in ['(','{','[']:
                stack.append(c)
            else:
                if len(stack) >0:
                    if stack[-1] == table[c]:
                        stack.pop()
                    else:
                        return False
                else:
                    return False
        return len(stack) == 0
