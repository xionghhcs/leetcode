class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        table = dict()
        for idx, item in enumerate(list1):
            table[item] = idx
        
        ans = []
        s_list = []
        min_idx_diff = 10000
        for idx, item in enumerate(list2):
            if item in table:
                s = idx + table[item]
                s_list.append(s)
                if s < min_idx_diff:
                    min_idx_diff = s
            else:
                s_list.append(100000)
        for idx, v in enumerate(s_list):
            if v == min_idx_diff:
                ans.append(list2[idx])
        return ans

