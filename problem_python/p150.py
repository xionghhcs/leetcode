class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for item in tokens:
            if item not in ['+','-','*','/']:
                stack.append(int(item))
            else:
                s2 = stack.pop()
                s1 = stack.pop()
                if item == '+':
                    res = s1 + s2
                elif item == '-':
                    res = s1 - s2
                elif item == '*':
                    res = s1 * s2
                else:
                    flag = 1
                    if s1 < 0:
                        flag = -flag
                        s1 = - s1
                    if s2 < 0:
                        flag = - flag
                        s2 = -s2
                    res = flag * (s1 // s2)
                stack.append(res)
        return stack.pop()
