class Solution(object):
    def getHint(self, secret, guess):
        secret = list(secret)
        guess = list(guess)
        bulls = 0
        l1,l2 = [0]*10,[0]*10
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                bulls+=1
            else:
                l1[int(secret[i])]+=1
                l2[int(guess[i])]+=1
        cows = sum([min(x,y) for x,y in zip(l1,l2)])
        return '%dA%dB' % (bulls, cows)
                
            
            
        
