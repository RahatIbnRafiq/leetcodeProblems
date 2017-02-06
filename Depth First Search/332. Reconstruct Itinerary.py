import collections
class Solution(object):

    def visit(self,airport):
        while self.targets[airport]:
            self.visit(self.targets[airport].pop())
        self.route.insert(0,airport)
        
    def findItinerary(self, tickets):
        self.targets = collections.defaultdict(list)
        for a, b in sorted(tickets)[::-1]:
            self.targets[a] += b,
        self.route = []
        self.visit("JFK")
        return self.route
