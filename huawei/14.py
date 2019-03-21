class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ''
        if len(strs) == 1:
            return strs[0]
        min_len = min([len(item) for item in strs])

        ans = []
        for col in range(min_len):
            flag = True
            for i in range(1, len(strs)):
                if strs[i-1][col] != strs[i][col]:
                    flag = False
                    break
            if flag is True:
                ans.append(strs[0][col])
            else:
                break
        return ''.join(ans)
