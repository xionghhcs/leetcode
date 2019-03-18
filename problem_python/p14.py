class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ''
        if len(strs) == 1:
            return strs[0]
        ans = []
        max_len = min([len(s) for s in strs])
        for i in range(max_len):
            flag = True
            for j in range(1, len(strs)):
                if strs[j][i] != strs[j-1][i]:
                    flag = False
                    break
            if flag is True:
                ans.append(strs[0][i])
            else:
                break
        return ''.join(ans)

            