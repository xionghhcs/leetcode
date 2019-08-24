class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        ans = []
        for w in A:
            d = dict()
            for c in w:
                d[c] = d.get(c, 0) + 1
            ans.append(d)
        res = list()
        for k in ans[0]:
            flag = True
            cnt = ans[0][k]
            for d in ans:
                if k in d:
                    if d[k] < cnt:
                        cnt = d[k]
                else:
                    flag = False
                    break
            if flag:
                for _ in range(cnt):
                    res.append(k)
        return res
    
                