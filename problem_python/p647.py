class Solution:
    def countSubstrings(self, s: str) -> int:
        def get_count(s, i, j):
            cnt = 0
            while i>=0 and j<len(s) and s[i]==s[j]:
                cnt += 1
                i-=1 
                j += 1
            return cnt
        
        ans = 0
        for i in range(len(s)):
            ans += get_count(s, i, i)
            ans += get_count(s, i, i+ 1)
        return ans

        