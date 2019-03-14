class Solution:
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        if num == 0:
            return [0]
        if num == 1:
            return [0, 1]
        ans = []
        ans.extend([0,1])
        k,i = 2,2
        while i <=num:
            i = 2 **(k-1)
            while i < 2**k:
                if i > num:
                    break
                
                t = (2**k - 2**(k-1)) // 2

                if i < 2**(k-1) + t:
                    ans.append(ans[i-t])
                else:
                    ans.append(ans[i-t] + 1)

                i += 1
            k += 1
        return ans[:num+1]
