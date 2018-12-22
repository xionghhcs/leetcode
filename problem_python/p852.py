class Solution(object):
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        i = 0 
        j = len(A) - 1 -1
        while i < len(A) - 1 and A[i] < A[i+1]:
            i += 1
        
        while j > 1 and A[j] < A[j - 1]:
            j -= 1
        
        return i

class Solution2(object):
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        for i in range(1, len(A) - 1):
            if A[i] > A[i-1] and A[i] > A[i+1]:
                return i