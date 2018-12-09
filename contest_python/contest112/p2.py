class Solution:
    def validateStackSequences(self, pushed, popped):
        """
        :type pushed: List[int]
        :type popped: List[int]
        :rtype: bool
        """
        stack = []
        for idx, v in enumerate(pushed):
            stack.append(v)
            while len(stack) > 0 and stack[-1] == popped[0]:
                del stack[-1]
                del popped[0]
        if len(stack) == 0:
            return True
        else:
            return False





