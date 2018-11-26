class Solution:
    def validateStackSequences(self, pushed, popped):
        """
        :type pushed: List[int]
        :type popped: List[int]
        :rtype: bool
        """
        value_dict = dict()
        for idx in range(len(pushed)):
            value_dict[pushed[idx]] = idx

        for idx, v in enumerate(pushed):
            pushed[idx] = value_dict[v]
        for idx, v in enumerate(popped):
            popped[idx] = value_dict[v]



