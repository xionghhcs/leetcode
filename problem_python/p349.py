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