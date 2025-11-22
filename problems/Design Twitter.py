from collections import defaultdict, deque
import heapq
from typing import List, Set, Deque, Tuple



# Wow I've dont it myself, feels good!
# But man it took more than 45 mins :skullllllll
# Lets speed it up next time

class User:

    def __init__(self):
        self.following: Set[int] = set()
        self.tweets: List[List[int]] = []

class Twitter:

    def __init__(self):
        self.users: dict[int, User] = defaultdict(User)
        self.tweetTimeStamp: int = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        # self.users[userId].posts.append(tweetId)
        self.users[userId].tweets.append([tweetId, self.tweetTimeStamp])
        self.tweetTimeStamp += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        postMaxHeap = []

        if userId not in self.users[userId].following:
            self.users[userId].following.add(userId)

        for followeeId in self.users[userId].following:
            followee = self.users[followeeId]
            for i in range(10):
                if i + 1 > len(followee.tweets):
                    break
                tweetId, timeStamp = followee.tweets[-1 - i]
                heapq.heappush(postMaxHeap, (-timeStamp, tweetId))
            

        newsFeed: List[int] = []
        count = 0
        while postMaxHeap and count < 10:
            newsFeed.append(heapq.heappop(postMaxHeap)[1])
            count += 1
        return newsFeed

    def follow(self, followerId: int, followeeId: int) -> None:
        self.users[followerId].following.add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        try:
            self.users[followerId].following.remove(followeeId)
        except:
            pass

    # def createUserIfNotExits(self, userId: int) -> None:
    #     if userId not in se


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)






# Using deque for better memory management

# Wow it's a personal acheivement it bet 100% of submissions :tears_in_joy
class User:

    def __init__(self):
        self.following: Set[int] = set()
        self.tweets: Deque[int] = deque(maxlen=10)

class Twitter:

    def __init__(self):
        self.users: dict[int, User] = defaultdict(User)
        self.tweetTimeStamp: int = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        # self.users[userId].posts.append(tweetId)
        self.users[userId].tweets.append([tweetId, self.tweetTimeStamp])
        self.tweetTimeStamp -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        minHeap: List[Tuple] = []

        self.users[userId].following.add(userId)

        for follwee in self.users[userId].following:
            if not self.users[follwee].tweets:
                continue
            idx = len(self.users[follwee].tweets) - 1
            tweetId, timeStamp = self.users[follwee].tweets[idx]
            minHeap.append((timeStamp, tweetId, follwee, idx))

        heapq.heapify(minHeap)

        newsFeed: List[int] = []
        while minHeap and len(newsFeed) < 10:
            timeStamp, tweetId, follwee, idx = heapq.heappop(minHeap)
            newsFeed.append(tweetId)

            if idx > 0:
                tweetId, timeStamp = self.users[follwee].tweets[idx - 1]
                heapq.heappush(minHeap, (timeStamp, tweetId, follwee, idx - 1))

        return newsFeed


    def follow(self, followerId: int, followeeId: int) -> None:
        self.users[followerId].following.add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.users[followerId].following:
            self.users[followerId].following.remove(followeeId)