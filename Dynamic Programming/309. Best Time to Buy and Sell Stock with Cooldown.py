class Solution(object):
    def maxProfit(self, prices):
        if len(prices) < 2: return 0
        buy = [0 for x in prices]
        sell = [0 for x in prices]
        cooldown = [0 for x in prices]
        buy[0] = -prices[0]
        for i in range(1,len(prices)):
            buy[i] = max(cooldown[i-1]-prices[i],buy[i-1])
            sell[i] = max(sell[i-1],buy[i-1]+prices[i])
            cooldown[i] = max(sell[i-1],buy[i-1],cooldown[i-1])
        return max(cooldown[-1],buy[-1],sell[-1])
        
