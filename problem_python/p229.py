class Solution:
    def majorityElement(self, nums: 'List[int]') -> 'List[int]':
        a = nums[0]
        b = nums[0]
        a_cnt = 0
        b_cnt = 0
        for v in nums:
            if v == a:
                a_cnt += 1
                continue
            if v == b:
                b_cnt += 1
                continue
            
            if a_cnt == 0:
                a = v
                a_cnt = 1
                continue
            
            if b_cnt == 0:
                b=v
                b_cnt = 1

                continue
            
            a_cnt -= 1
            b_cnt -= 1
        
        a_cnt = 0
        b_cnt = 0
        for v in nums:
            if v == a:
                a_cnt += 1
            elif v == b:
                b_cnt += 1
        ans = []
        if a_cnt > len(nums) // 3:
            ans.append(a)
        if b_cnt > len(nums) // 3:
            ans.append(b)
        return ans

    