import heapq
class Twitter(object):

    def __init__(self):
        self.followmap = dict()
        self.tweetmap = dict()
        self.time = -1
        

    def postTweet(self, userId, tweetId):
        try:
            self.time += 1
            self.tweetmap[userId] = self.tweetmap.get(userId,[])+[(self.time,tweetId)]
        except Exception:
            return
        

    def getNewsFeed(self, userId):
        tweets = []
        users = [userId]
        if userId in self.followmap:
            for user in self.followmap[userId]:
                users = users + [user]
                
        for user in users:
            if user in self.tweetmap:
                for tweet in self.tweetmap[user]:
                    heapq.heappush(tweets,tweet)

        return [x[1] for x in heapq.nlargest(10,tweets)]
        

    def follow(self, followerId, followeeId):
        if followerId != followeeId:
            self.followmap[followerId] = self.followmap.get(followerId,[])+[followeeId]
            self.followmap[followerId] = list(set(self.followmap[followerId]))
        

    def unfollow(self, followerId, followeeId):
        try:
            self.followmap[followerId].remove(followeeId)
        except Exception:
            return
