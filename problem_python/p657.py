class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        num = dict()
        num['U'] = 0
        num['D'] = 0
        num['L'] = 0
        num['R'] = 0
        for m in moves:
            num[m] += 1
        if num['U'] == num['D'] and num['L'] == num['R']:
            return True
        else:
            return False