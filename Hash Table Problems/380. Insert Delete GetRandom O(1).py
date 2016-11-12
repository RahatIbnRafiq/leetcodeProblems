from random import randint
class RandomizedSet(object):

    def __init__(self):
        self.nums,self.map = [],{}
        

    def insert(self, val):
        if val not in self.map:
            self.nums = self.nums + [val]
            self.map[val]  = len(self.nums)-1
            return True
        return False
        

    def remove(self, val):
        if val in self.map:
            idx, last = self.map[val], self.nums[-1]
            self.nums[idx], self.map[last] = last,idx
            self.nums.pop(); self.map.pop(val, 0)
            return True
        return False
            
        

    def getRandom(self):
        return self.nums[random.randint(0, len(self.nums) - 1)]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
