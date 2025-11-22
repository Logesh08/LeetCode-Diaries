# [355. Design Twitter](https://leetcode.com/problems/design-twitter/description/)

Design a simplified version of Twitter where users can post tweets, follow/unfollow another user, and is able to see the <code>10</code> most recent tweets in the user's news feed.

Implement the <code>Twitter</code> class:

- <code>Twitter()</code> Initializes your twitter object.
- <code>void postTweet(int userId, int tweetId)</code> Composes a new tweet with ID <code>tweetId</code> by the user <code>userId</code>. Each call to this function will be made with a unique <code>tweetId</code>.
- <code>List<Integer> getNewsFeed(int userId)</code> Retrieves the <code>10</code> most recent tweet IDs in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user themself. Tweets must be **ordered from most recent to least recent** .
- <code>void follow(int followerId, int followeeId)</code> The user with ID <code>followerId</code> started following the user with ID <code>followeeId</code>.
- <code>void unfollow(int followerId, int followeeId)</code> The user with ID <code>followerId</code> started unfollowing the user with ID <code>followeeId</code>.

**Example 1:** 

```
Input

["Twitter", "postTweet", "getNewsFeed", "follow", "postTweet", "getNewsFeed", "unfollow", "getNewsFeed"]
[[], [1, 5], [1], [1, 2], [2, 6], [1], [1, 2], [1]]
Output

[null, null, [5], null, null, [6, 5], null, [5]]

Explanation

Twitter twitter = new Twitter();
twitter.postTweet(1, 5); // User 1 posts a new tweet (id = 5).
twitter.getNewsFeed(1);  // User 1's news feed should return a list with 1 tweet id -> [5]. return [5]
twitter.follow(1, 2);    // User 1 follows user 2.
twitter.postTweet(2, 6); // User 2 posts a new tweet (id = 6).
twitter.getNewsFeed(1);  // User 1's news feed should return a list with 2 tweet ids -> [6, 5]. Tweet id 6 should precede tweet id 5 because it is posted after tweet id 5.
twitter.unfollow(1, 2);  // User 1 unfollows user 2.
twitter.getNewsFeed(1);  // User 1's news feed should return a list with 1 tweet id -> [5], since user 1 is no longer following user 2.
```

**Constraints:** 

- <code>1 <= userId, followerId, followeeId <= 500</code>
- <code>0 <= tweetId <= 10^4</code>
- All the tweets have **unique**  IDs.
- At most <code>3 * 10^4</code> calls will be made to <code>postTweet</code>, <code>getNewsFeed</code>, <code>follow</code>, and <code>unfollow</code>.
- A user cannot follow himself.

---

## Solution

```python
class User:

    def __init__(self):
        self.following: Set[int] = set()
        self.tweets: List[Deque[int]] = deque(maxlen=10)

class Twitter:

    def __init__(self):
        self.users: dict[int, User] = defaultdict(User)
        self.tweetTimeStamp: int = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.users[userId].tweets.append([tweetId, self.tweetTimeStamp])
        self.tweetTimeStamp -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        minHeap: List[Tuple] = []

        if userId not in self.users[userId].following:
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
```