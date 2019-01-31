class Solution:
    def longestWord(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        if not words:
            return ''
        words.sort()
        st = set()
        res = ''
        for w in words:
            if len(w) == 1:
                st.add(w)
                if res == '':
                    res += w
            elif w[:-1] in st:
                st.add(w)
                if len(res) < len(w):
                    res = w
        return res