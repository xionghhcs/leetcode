class Solution:
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        if len(chars) == 1:
            return 1
        pre = chars[0]
        ans = []
        ans.append(pre)
        cnt = 1
        for i in range(1, len(chars)):
            if chars[i] == pre:
                cnt += 1
            else:
                ans.append(str(cnt))
                pre = chars[i]
                ans.append(pre)
                cnt = 1
        for i, v in enumerate(ans):
            chars[i] = v
        return len(ans)
