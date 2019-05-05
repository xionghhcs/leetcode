class Solution:
    def reverseWords(self, s: str) -> str:
        ans = []
        i = 0
        while i < len(s):
            if s[i] != ' ':
                j = i + 1
                while j < len(s) and s[j] != ' ':
                    j += 1
                ans.append(s[i:j])
                i = j
            else:
                i += 1
        ans = ans[::-1]
        return ' '.join(ans)
