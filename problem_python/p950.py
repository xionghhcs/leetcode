class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        idx = []
        for i in range(len(deck)):
            idx.append(i)
        res = [0] * len(deck)
        deck.sort()
        for c in deck:
            tmp = idx[0]
            del idx[0]
            res[tmp] = c
            if len(idx) > 0:
                idx.append(idx[0])
                del idx[0]
        return res
    