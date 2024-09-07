class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:


        hashans = defaultdict(int)
        res = 0
        for t in time:
            rem = t % 60
            complement = (60 - rem) % 60  # This handles rem == 0 correctly
            
            # Add to result the count of times we have seen this complement
            res += hashans[complement]

            # Add current remainder to the hash for future matches
            hashans[rem] += 1

        return res
                