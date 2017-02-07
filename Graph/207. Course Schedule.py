class Solution(object):

    def helper(self,course):
        self.grey.append(course)
        if course in self.graph:
            for kid in self.graph[course]:
                if kid in self.grey:
                    self.result = False
                    return
                if kid not in self.black:
                    self.helper(kid)
        self.black.append(course)
        self.grey.remove(course)
        
    def canFinish(self, numCourses, prerequisites):
        self.result = True
        self.black = []
        self.grey = []
        self.graph = dict()
        for x in prerequisites:
            a,b = x[0],x[1]
            self.graph[x[1]] = self.graph.get(x[1],[])+[x[0]]

        for i in range(0,numCourses):
            if i not in self.black:
                self.helper(i)
        return self.result
