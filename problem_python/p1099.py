class Solution:
    def twoSumLessThanK(self, A: List[int], K: int) -> int:
        A.sort()
        i = 0
        j = len(A) - 1
        ans = -1
        while i < j:
            cur_s = A[i] + A[j]
            
            if cur_s < K:
                if cur_s > ans:
                    ans = cur_s
                i += 1
            else:
                j -= 1
        return ans
