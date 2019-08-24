class Solution(object):
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        ans = []
        for col in zip(*A):
            ans.append(col)
        return ans

class Solution2:
    def transpose(self, A: List[List[int]]) -> List[List[int]]:
        m, n = len(A), len(A[0])
        ans = [[0] * m for _ in range(n)]
        
        for i in range(m):
            for j in range(n):
                ans[j][i] = A[i][j]
        return ans
    
        
