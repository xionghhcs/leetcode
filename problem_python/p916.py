class Solution:
    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        aDict = []
        bDict = []
        for w in A:
            d = dict()
            for c in w:
                d[c] =d.get(c, 0) + 1
            aDict.append(d)
        for w in B:
            d = dict()
            for c in w:
                d[c] = d.get(c, 0) + 1
            bDict.append(d)
            
        judge = dict()
        for item in bDict:
            for k in item:
                if k not in judge or item[k] > judge[k]:
                    judge[k] = item[k]

        ans = []
        for i in range(len(A)):
            flag = True
            for k in judge:
                if k not in aDict[i] or judge[k] > aDict[i][k]:
                    flag = False
                    break
            if flag:
                ans.append(A[i])
        return ans
    