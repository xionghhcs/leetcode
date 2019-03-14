class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        new_strs = list(map(lambda x: ''.join(sorted(list(x))), strs))
        import collections
        table = collections.defaultdict(list)
        for idx, item in enumerate(new_strs):
            table[item].append(strs[idx])
        ans = []
        for key in table:
            ans.append(table[key])
        return ans


class Solution2:
    def groupAnagrams(self, strs):
        import collections
        table = collections.defaultdict(list)
        for s in strs:
            cnt = [0] * 26
            for c in s:
                cnt[ord(c) - ord('a')] += 1
            key = ''.join(list(map(str, cnt)))
            table[key].append(s)
        ans = []
        for key in table:
            ans.append(table[key])
        return ans
