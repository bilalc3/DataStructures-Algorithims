from collections import Counter
import heapq
from typing import List

class SolutionHP:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # priority queue 
        # time complexity: O(T Log T ) or O(N) 
        counter = Counter(tasks)
        max_heap = [(-count, task) for task, count in counter.items()]
        heapq.heapify(max_heap)
        
        time = 0
        queue = []

        while max_heap or queue:
            time += 1

            if max_heap:
                count, task = heapq.heappop(max_heap)
                count += 1
                if count != 0:
                    queue.append((count, task, time + n))
            
            if queue and queue[0][2] == time:
                heapq.heappush(max_heap, queue.pop(0)[:2])
        
        return time


