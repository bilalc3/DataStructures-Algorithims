class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        n1n2 = defaultdict(int)
        n3n4 = defaultdict(int)

        for first in nums1:
            for second in nums2:
                n1n2[first + second] += 1

        for first in nums3:
            for second in nums4:
                n3n4[first + second] += 1

        total_sum = 0
        for k, v in n1n2.items():
            if -k in n3n4:
                total_sum += (v * n3n4[-k])
            
        
        return total_sum
        

