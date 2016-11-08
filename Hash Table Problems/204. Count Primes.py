class Solution(object):
    def countPrimes(self, n):
        if n < 2:return 0
        isPrime = [1]*(n)
        isPrime[0],isPrime[1] = 0,0
        i = 2
        while i*i < n:
            if isPrime[i] == 0:
                i+=1
                continue
            j = i*i
            while j < n:
                isPrime[j]=0
                j +=i
            i+=1
            
        return sum(isPrime)
        
