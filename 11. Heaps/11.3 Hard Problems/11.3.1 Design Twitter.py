"""
Q. Design a simplified version of Twitter where users can post tweets, follow/unfollow another user, and is able to see the 10 most recent tweets in the user's news feed.

Implement the Twitter class:

Twitter() Initializes your twitter object.
void postTweet(int userId, int tweetId) Composes a new tweet with ID tweetId by the user userId. Each call to this function will be made with a unique tweetId.
List<Integer> getNewsFeed(int userId) Retrieves the 10 most recent tweet IDs in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user themself. Tweets must be ordered from most recent to least recent.
void follow(int followerId, int followeeId) The user with ID followerId started following the user with ID followeeId.
void unfollow(int followerId, int followeeId) The user with ID followerId started unfollowing the user with ID followeeId.
 

Example 1:

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
"""
import heapq

class Twitter:

    def __init__(self):
        self.users = {}
        self.tweets = {}
        self.auto = 0

    def postTweet(self, userId: int, tweetId: int):
        if userId not in self.tweets:
            self.auto += 1
            self.tweets[userId] = [(self.auto, tweetId)]
        else:
            self.auto += 1
            self.tweets[userId].append((self.auto, tweetId))

    def getNewsFeed(self, userId: int):
        heap = []
        heap.extend(self.tweets.get(userId, []))
        for user in self.users.get(userId, {}):
            heap.extend(self.tweets.get(user, []))
        heap = [(-val[0], val[1]) for val in heap]
        heapq.heapify(heap)
        counter = 1
        ans = []

        while heap and counter <= 10:
            ans.append(heapq.heappop(heap)[1])
            counter += 1
        return ans
        

    def follow(self, followerId: int, followeeId: int):
        if followerId == followeeId:
            return
        if followeeId not in self.users:
            self.users[followerId] = {followeeId}
        else:
            self.users[followerId].add(followeeId)


    def unfollow(self, followerId: int, followeeId: int):
        if followerId not in self.users:
            return
        if followeeId in self.users[followerId]:
            self.users[followerId].remove(followeeId)
        


twitter = Twitter()
twitter.postTweet(1, 6)
print(twitter.getNewsFeed(1))
twitter.follow(1, 2)
twitter.postTweet(2, 5)
print(twitter.getNewsFeed(1))
twitter.unfollow(1, 2)
print(twitter.getNewsFeed(1))