class Solution:
    def shortestDistance(self, words: List[str], word1: str, word2: str) -> int:
        ans = len(words)
        w1Idx = -1
        w2Idx = -1
        for i in range(len(words)):
            if words[i] == word1:
                w1Idx = i
                if w2Idx != -1:
                    ans = min(ans, abs(w2Idx - w1Idx))
            elif words[i] == word2:
                w2Idx = i
                if w1Idx != -1:
                    ans = min(ans, abs(w2Idx - w1Idx))
        return ans
    