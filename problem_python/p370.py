class Solution:
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        ans = [0] * length
        for item in updates:
            ans[item[0]] += item[2]
            if item[1] + 1 < length:
                ans[item[1]+1] -= item[2]

        for i in range(1, length):
            ans[i] = ans[i] + ans[i-1]

        return ans
    