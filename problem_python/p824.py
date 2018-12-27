class Solution:
    def toGoatLatin(self, S):
        """
        :type S: str
        :rtype: str
        """
        vowel = 'aeiouAEIOU'
        result = []
        for i, w in enumerate( S.split(' '), start=1):
            if w[0] in vowel:
                result.append(w + 'ma' + 'a' * i)
            else:
                result.append(w[1:] + w[:1] + 'ma' + 'a' * i)
        return ' '.join(result)