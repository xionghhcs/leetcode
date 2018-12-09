class Solution:
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        for i in range(1, len(words)):
            if self.cmp(words[i-1], words[i], order) is False:
                return False
        return True

    def cmp(self, w1, w2, order):
        w1_ids = [order.find(c) for c in w1]
        w2_ids = [order.find(c) for c in w2]
        minlen = min(len(w1_ids), len(w2_ids))
        for i in range(minlen):
            if w1_ids[i] < w2_ids[i]:
                return True
            elif w1_ids[i] > w2_ids[i]:
                return False
        if len(w1) <= len(w2):
            return True
        else:
            return False
