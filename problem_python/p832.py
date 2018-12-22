class Solution(object):
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        for i in range(len(A)):
            A[i] = A[i][::-1]
            for j in range(len(A[0])):
                A[i][j] = 0 if A[i][j] == 1 else 1
        return A