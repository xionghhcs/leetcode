class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        alphabet = ['qwertyuiop', 'asdfghjkl', 'zxcvbnm']
        ans = []
        for w in words:
            idx = 0
            w_lower = w.lower()
            for bet in alphabet:
                if w_lower[0] in bet:
                    break
                idx += 1
            for c in w_lower:
                if c not in alphabet[idx]:
                    break
            else:
                ans.append(w)
        return ans