class Solution:
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        INF = 100000
        def find_left(s, c, i):
            if s[i] == c:
                return 0
            ans = 0
            tmp = i
            while i >=0 and s[i] != c:
                i -= 1
            if i == -1:
                return INF
            else:
                return tmp - i
        
        def find_right(s, c, i):
            if s[i] == c:
                return 0
            ans = 0
            tmp = i
            while i <len(s) and s[i] != c:
                i += 1
            if i == len(s):
                return INF
            else:
                return i - tmp
        

        ans = []
        for i in range(len(S)):
            if i == 0:
                res = find_right(S, C, 0)
            elif i == len(S) - 1:
                res = find_left(S, C, len(S) - 1)
            else:
                res = min(find_left(S,C, i), find_right(S, C, i))
            ans.append(res)
        return ans