class Solution:
    def permute(self, nums):
        position = [0] * len(nums)
        import copy
        def get_permute(row, ans):
            if len(row) == len(nums):
                ans.append(copy.deepcopy(row))
            else:
                for i in range(len(nums)):
                    if position[i] == 0:
                        position[i] = 1
                        row.append(nums[i])
                        get_permute(row, ans)
                        row.pop()
                        position[i] = 0
        ans = []
        row = []
        get_permute(row, ans)
        return ans

so = Solution()
print(so.permute([1,2,3]))


