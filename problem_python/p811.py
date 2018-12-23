class Solution(object):
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        cnt_table = dict()
        for address in cpdomains:
            cnt = int(address.split(' ')[0])
            addr = address.split(' ')[1]
            addrs = addr.split('.')
            addrs = addrs[::-1]
            postfix = ''
            for item in addrs:
                if postfix == '':
                    postfix = item
                else:
                    postfix = item +'.'+ postfix
                
                if postfix in cnt_table:
                    cnt_table[postfix] += cnt
                else:
                    cnt_table[postfix] = cnt
        ans = []    
        for k in cnt_table:
            ans.append('{} {}'.format(cnt_table[k], k))
        return ans
                