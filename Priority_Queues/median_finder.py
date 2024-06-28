import heapq


class MedianFinder:


    # cases
    # if num belongs in small and size equals we good 
    # id num beloings in samlla nd size imalablcen, pop off small and put in big 

    # if num belogns in big and size equals we good to add 
    # if num, bnelogns in big and size imbalance, pop off big and add to small 

    def __init__(self):
        self.small, self.large = [], []

    def addNum(self, num: int) -> None:
        if self.large and num > self.large[0]:
            heapq.heappush(self.large, num)
        else:
            heapq.heappush(self.small, -1 * num)

        
        if len(self.small) - len(self.large) > 1:
            # too many in small
            elem = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, elem)
        elif len(self.large) - len(self.small) > 1:
            elem = heapq.heappop(self.large )
            heapq.heappush(self.small, - elem)


    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -self.small[0]
        elif len(self.large) > len(self.small):
            return self.large[0]
        else:
            return (-self.small[0] + self.large[0]) / 2.0
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()