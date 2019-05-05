class Solution:
    def groupAnagrams(self, strs):
        import copy
        strs_cp = copy.deepcopy(strs)
        for i, item in enumerate(strs_cp):
            item = list(item)
            item.sort()
            item = ''.join(item)
            strs_cp[i] = item
        table = dict()
        for i, item in enumerate(strs_cp):
            if item not in table:
                table[item] = []
            table[item].append(strs[i])
        ans = []
        for k in table:
            ans.append(table[k])
        return ans
