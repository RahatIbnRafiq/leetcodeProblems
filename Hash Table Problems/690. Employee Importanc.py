"""
# Employee info
class Employee(object):
    def __init__(self, id, importance, subordinates):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates
"""
class Solution(object):
    
    def dfs(self,eid):
        sub_imp = sum([self.dfs(sub_id) for sub_id in self.m[eid].subordinates])
        return self.m[eid].importance+sub_imp
        
    def getImportance(self, employees, id):
        self.m = {e.id:e for e in employees}
        return self.dfs(id)
        
