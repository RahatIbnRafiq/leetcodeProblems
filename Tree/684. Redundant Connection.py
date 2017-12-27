class DU(object):
    def __init__(self):
        self.parents = range(1001)
        self.rank = [0] * 1001

    def find(self, x):
        if self.parents[x] != x:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

    def union(self, x, y):
        xp, yp = self.find(x), self.find(y)
        if xp == yp:
            return False
        elif self.rank[xp] < self.rank[yp]:
            self.parents[xp] = yp
        elif self.rank[xp] > self.rank[yp]:
            self.parents[yp] = xp
        else:
            self.parents[yp] = xp
            self.rank[xp] += 1
        return True



class Solution(object):

    def findRedundantConnection(self, edges):
        du = DU()
        for edge in edges:
            if not du.union(edge[0],edge[1]):
                return edge

            
        

            
        
            
        
