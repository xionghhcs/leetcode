class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        t1, t2 = dict(), dict()
        for i in nums1:
            t1[i] = 1
        for i in nums2:
            t2[i] = 1
        ans = []
        for k in t1:
            if k in t2:
                ans.append(k)
        return ans

class Solution2:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        ans = []
        i,j = 0, 0
        while i< len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                if len(ans) > 0 and ans[-1] == nums1[i]:
                    i += 1
                    j += 1
                    continue
                ans.append(nums1[i])
                i += 1
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1
        return ans
      