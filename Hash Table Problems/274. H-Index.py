class Solution(object):
    def hIndex(self, citations):
        length = len(citations)
        count = [0]*(length+1)
        for c in citations:
            if c > length:count[-1]+=1
            else:count[c]+=1
        for i in range(length-1,-1,-1):
            count[i] = count[i]+count[i+1]
        for i in range(length,-1,-1):
            if count[i]>=i:return i
        return count[0]
