class RecentCounter(object):

    def __init__(self):
        self.pings = []

    def ping(self, t):
        """
        :type t: int
        :rtype: int
        """
        from bisect import bisect_left
        self.pings.append(t)
        index = bisect_left(self.pings, t-3000)
        return len(self.pings) - index
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)