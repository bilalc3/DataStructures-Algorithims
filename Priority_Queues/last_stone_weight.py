import heapq
from typing import List


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        neg_stones = [-x for x in stones]
    
        print(neg_stones)
        heapq.heapify(neg_stones)


        while len(neg_stones) != 1:
            x = -heapq.heappop(neg_stones)
            y = -heapq.heappop(neg_stones)
            if x == y:
                heapq.heappush(neg_stones, 0)
            else:
                z = max(y, x) - min(x, y)
                heapq.heappush(neg_stones, -z)
        
        return -neg_stones[0]
