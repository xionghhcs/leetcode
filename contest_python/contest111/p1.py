class Solution:
    def validMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        if len(A) <3:
            return False
        max_a1 = -1
        max_idx1 = -1
        for idx, a in enumerate(A):
            if a > max_a1:
                max_a1 = a
                max_idx1 = idx
            else:
                break

        max_a2 = -1
        max_idx2 = -1
        for idx, a in enumerate(reversed(A)):
            if a > max_a2:
                max_a2 = a
                max_idx2 = idx
            else:
                break
        if max_idx1 == 0 or max_idx1 == len(A) - 1:
            return False
        if max_idx2 == 0 or max_idx2 == len(A)-1:
            return False
        return max_a1 == max_a2 and max_idx1 + max_idx2 == len(A) - 1


class Solution2:
    def validMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        pass