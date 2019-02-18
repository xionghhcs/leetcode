class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        hash_table = dict()
        for i in nums:
            try:
                hash_table[i] += 1
            except:
                hash_table[i] = 1
        threshold = len(nums) // 2
        for key in hash_table:
            if hash_table[key] > threshold:
                return key

class Solution2:
    def majorityElement(self, nums):
        cur = nums[0]
        cnt = 0
        for v in nums:
            if cnt == 0:
                cur = v
                cnt = 1
            else:
                if cur == v:
                    cnt += 1
                else:
                    cnt -= 1
        return cur
    
            