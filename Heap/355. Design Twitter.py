import heapq
class Twitter(object):
    def __init__(self):
        self.followmap = dict()
        self.tweetmap = dict()
        self.time = -1
        
    def postTweet(self, userId, tweetId):
        self.time+=1
        self.tweetmap[userId] = self.tweetmap.get(userId,[])+[(self.time,tweetId)]
        
    def getNewsFeed(self, userId):
        try:
            users = self.followmap[userId]+[userId]
        except Exception:
            users = [userId]
        users = list(set(users))
        tweets = []
        for user in users:
            if user in self.tweetmap:
                tweets = tweets + self.tweetmap[user]
        heapq.heapify(tweets)
        return [x[1] for x in heapq.nlargest(10,tweets)]

    def follow(self, followerId, followeeId):
        self.followmap[followerId] = self.followmap.get(followerId,[])+[followeeId]
        
    def unfollow(self, followerId, followeeId):
        try:
            self.followmap[followerId].remove(followeeId)
        except Exception:
            return


twitter = Twitter()
twitter.postTweet(1, 1)
print twitter.getNewsFeed(1)
twitter.follow(2, 1)
print twitter.getNewsFeed(2)
twitter.unfollow(2, 1)
print twitter.getNewsFeed(2)
