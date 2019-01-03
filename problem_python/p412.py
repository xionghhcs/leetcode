class Solution:
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ans = []
        for i in range(1, n+1):
            if i % 3 == 0 and i % 5 != 0:
                ans.append('Fizz')
                continue
            if i % 3 != 0 and i % 5 == 0:
                ans.append('Buzz')
                continue
            
            if i % 3 == 0 and i % 5 == 0:
                ans.append('FizzBuzz')
                continue
            
            ans.append(str(i))
        return ans