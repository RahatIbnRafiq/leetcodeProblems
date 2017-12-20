class MapSum(object):

    def __init__(self):
        self.dict = dict()
        

    def insert(self, key, val):
        self.dict[key] = val
        

    def sum(self, prefix):
        result = 0
        for key in self.dict.keys():
            if len(key) >= len(prefix) and prefix == key[0:len(prefix)]:
                result += self.dict.get(key)
        return result
        


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)
