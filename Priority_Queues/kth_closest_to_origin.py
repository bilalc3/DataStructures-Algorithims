from typing import List 
import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        minheap = []

        # augment the data with heap 
        for (x , y) in points:
            distance = x ** 2 + y ** 2
            minheap.append((distance, (x, y)))
        
        
        heapq.heapify(minheap)
        
        # now that we have it assembled we pop off the frist k
        ans = []

        # pop off first k and dissemble heap
        for i in range(k):
            dist, point = heapq.heappop(minheap)
            ans.append(point)
        
        return ans
        

        




        