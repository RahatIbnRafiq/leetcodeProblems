class Solution(object):
    def maxProfit(self, prices):
        if not prices:return 0
        buy = [0 for x in prices]
        sell = [0 for x in prices]
        buy[0] = -prices[0]
        for i in xrange(1,len(prices)):
            buy[i] = max(buy[i-1],-prices[i])
            sell[i] = prices[i]+buy[i-1]
        return max(sell)

s = Solution()
print s.maxProfit([7,1,5,3,6,4])
