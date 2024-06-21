import heapq
from typing import List

class KthLargest:

    # takeaways
    '''
        use heapq utliity to intiate a minheap 
        can covert to max heap by reversing the data points 
        heapq.heapop, heapq.heappush, heapq.heapify
    '''

    def __init__(self, k: int, nums: List[int]):
        self.minheap, self.k = nums, k
        heapq.heapify(self.minheap)

    

    def add(self, val: int) -> int:
        # adding in first 
        heapq.heappush(self.minheap, val)

        # popping off everything that is exceed more than k
        while len(self.minheap) > self.k:
            heapq.heappop(self.minheap)
        
        return self.minheap[0]
