class Solution:
    def shortestWordDistance(self, words: List[str], word1: str, word2: str) -> int:
        w1Idx = -1
        w2Idx = -1
        ans = len(words)
        for i in range(len(words)):
            if word1 == word2 and words[i] == word1:
                if w1Idx < w2Idx:
                    w1Idx = i
                else:
                    w2Idx = i
                if w1Idx != -1 and w2Idx != -1:
                    ans = min(ans, abs(w1Idx - w2Idx))
            else:
                if words[i] == word1:
                    w1Idx = i
                    if w2Idx != -1:
                        ans = min(ans, abs(w2Idx - w1Idx))
                elif words[i] == word2:
                    w2Idx = i
                    if w1Idx != -1:
                        ans = min(ans, abs(w2Idx - w1Idx))
        return ans
