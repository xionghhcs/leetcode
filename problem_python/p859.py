class Solution:
    def buddyStrings(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        # if A == B:
        #     return False
        if len(A) != len(B):
            return False
        
        if A == B:
            if len(set(A)) < len(A):
                return True
            if len(set(A)) == len(A):
                return False
        
        indexs = []
        for i in range(len(A)):
            if A[i] != B[i]:
                indexs.append(i)
        
        if len(indexs) != 2:
            return False
        i = indexs[0]
        j = indexs[1]

        if A[i] == B[j] and A[j] == B[i]:
            return True

        return False
