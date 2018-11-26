class Solution:
    def diStringMatch(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        result = []
        min_v = 0
        max_v = len(S)
        for c in S:
            if c == 'I':
                result.append(min_v)
                min_v += 1
            else:
                result.append(max_v)
                max_v -= 1
        while min_v < max_v:
            result.append(min_v)
            min_v += 1
        return result