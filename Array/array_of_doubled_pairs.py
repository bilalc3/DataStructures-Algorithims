class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        arr.sort()
        hashmap = defaultdict(int)
        res = True

        for n in arr:
            if n in hashmap and hashmap[n] > 0:
                hashmap[n] -= 1
            elif n < 0:
                hashmap[n * 0.5] += 1
            elif n == 0:
                hashmap[0] += 1
            elif n > 0:
                hashmap[n * 2] += 1
        
        if not all(v == 0 for v in hashmap.values()):
            return False

        return True


        