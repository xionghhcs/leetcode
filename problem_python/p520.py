class Solution:
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        import string
        # print(string.ascii_uppercase)
        if word[0] in string.ascii_uppercase:
            if len(word)== 1:
                return True
            upper_cnt = 0
            for c in word:
                if c in string.ascii_uppercase:
                    upper_cnt += 1
            if upper_cnt == len(word) or upper_cnt == 1:
                return True
            return False
        else:
            for c in word:
                if c in string.ascii_uppercase:
                    return False
            return True