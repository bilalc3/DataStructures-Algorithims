import heapq
from collections import defaultdict
from typing import List

class Twitter:

    def __init__(self):
        self.count = 0
        self.tweetMap = defaultdict(list)  # userId -> list of [count, tweetIds]
        self.followMap = defaultdict(set)  # userId -> set of followeeId


    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append([self.count, tweetId])
        self.count -= 1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        # we can mimic a map reduce, like for each make it min heap and then take out best out of all 10 
        # or extent them into on ebig array and then run heapofu and pop. off the latest 10

        # we choose to take optimized path take f log f runtime, f being follower length which can be n 
        
        res = []
        minheap = []
        self.followMap[userId].add(userId)
        
        for followeeId in self.followMap[userId]:
            if followeeId in self.tweetMap and len(self.tweetMap[followeeId]) > 0:
                index = len(self.tweetMap[followeeId]) - 1
                c, tid = self.tweetMap[followeeId][index]
                heapq.heappush(minheap, (c, tid, followeeId, index - 1))
        
        while minheap and len(res) < 10:
            c, tid, followeeId, i = heapq.heappop(minheap)
            res.append(tid)
            if i >= 0:
                newc, newtid = self.tweetMap[followeeId][i]
                heapq.heappush(minheap, (newc, newtid, followeeId, i - 1))
        
        return res


    def follow(self, followerId: int, followeeId: int) -> None:
        # Add followerId in followeeId set
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)

# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId, tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId, followeeId)
# obj.unfollow(followerId, followeeId)
