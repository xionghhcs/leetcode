class Solution:
    def numSubarraysWithSum(self, A, S):
        """
        :type A: List[int]
        :type S: int
        :rtype: int
        """
        data_size = len(A)
        ans = 0
        for i in range(data_size):
            tmp_sum = 0
            for j in range(i, data_size):
                tmp_sum += A[j]
                if tmp_sum == S:
                    ans += 1
                elif tmp_sum > S:
                    break
            if tmp_sum < S:
                break
        return ans


class Solution2:
    def numSubarraysWithSum(self, A, S):
        """
        :type A: List[int]
        :type S: int
        :rtype: int
        """
        data_size = len(A)
        ans = 0
        from collections import defaultdict

        hmap = defaultdict(int)
        tmp_sum = 0
        for v in A:
            tmp_sum += v
            if tmp_sum == S:
                ans += 1
            if tmp_sum - S in hmap:
                ans += hmap.get(tmp_sum - S)
            hmap[tmp_sum] += 1
        return ans
