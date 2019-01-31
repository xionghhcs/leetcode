class Solution:
    def rotateString(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        if A == B:
            return True
        if len(A) != len(B) or len(A) == 1:
            return False
        
        size = len(A)
        for i in range(size):
            A = A[1:] + A[:1]
            if A == B:
                return True
        return False