class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []
            
        d = dict()
        d['2'] = 'abc'
        d['3'] = 'def'
        d['4'] = 'ghi'
        d['5'] = 'jkl'
        d['6'] = 'mno'
        d['7'] = 'pqrs'
        d['8'] = 'tuv'
        d['9'] = 'wxyz'
        ans = ['']
        for dig in digits:
            tmp_list = []
            for a in ans:
                for c in d[dig]:
                    tmp_list.append(a + c)
            ans = tmp_list
        return ans

