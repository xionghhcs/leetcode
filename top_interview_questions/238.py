class Solution:
    def productExceptSelf(self, nums):
        if nums is None or len(nums) == 0:
            return nums
        
        pre_product = 1
        import copy
        ans = copy.deepcopy(nums)
        for i in range(len(nums)):
            if i == 0:
                cur_product = pre_product
            else:
                cur_product = nums[i - 1] * pre_product
            
            ans[i] = cur_product

            pre_product = cur_product
        pre_product = 1

        for i in range(len(nums) - 1, -1, -1):
            if i == len(nums) - 1:
                cur_product = pre_product
            else:
                cur_product = pre_product * nums[i + 1]
            ans[i] *= cur_product
            pre_product = cur_product
        
        return ans

so = Solution()
print(so.productExceptSelf([1,2,3,4]))