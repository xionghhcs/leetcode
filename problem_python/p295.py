import heapq

class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.minheap = []
        self.maxheap = []

    def addNum(self, num: int) -> None:
        if len(self.maxheap) > len(self.minheap):
            heapq.heappush(self.minheap, num)
        else:
            heapq.heappush(self.maxheap, -num)
            
        if len(self.maxheap) + len(self.minheap) <= 1:
            return
        
        if -self.maxheap[0] > self.minheap[0]:
            max_ = -heapq.heappop(self.maxheap)
            min_ = heapq.heappop(self.minheap)
            heapq.heappush(self.maxheap, -min_)
            heapq.heappush(self.minheap, max_)

    def findMedian(self) -> float:
        if len(self.maxheap) > len(self.minheap):
            return -self.maxheap[0]
        else:
            return (-self.maxheap[0] + self.minheap[0]) / 2

        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()