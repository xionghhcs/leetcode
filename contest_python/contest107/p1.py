

class Solution:
    def isLongPressedName(self, name, typed):
        """
        :type name: str
        :type typed: str
        :rtype: bool
        """
        c1_cnt = list()
        c1_cnt.append([name[0], 1])
        for idx, c in enumerate(name[1:]):
            if c == name[idx - 1]:
                c1_cnt[-1][-1] += 1
                pass
            else:
                c1_cnt.append([c, 1])
        c2_cnt = list()
        c2_cnt.append([typed[0], 1])
        for idx, c in enumerate(typed[1:]):
            if c == typed[idx - 1]:
                c2_cnt[-1][-1] += 1
            else:
                c2_cnt.append([c,1])
        if len(c1_cnt) != len(c2_cnt):
            return False
        else:
            for idx in range(len(c1_cnt)):
                if c1_cnt[idx][0] != c2_cnt[idx][0]:
                    return False
                elif c1_cnt[idx][1] > c2_cnt[idx][1]:
                    return False
            return True