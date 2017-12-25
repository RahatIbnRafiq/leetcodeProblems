class MagicDictionary(object):

    def __init__(self):
        self.dict = dict()
        

    def buildDict(self, dict):
        for word in dict:
            self.dict[len(word)] = self.dict.get(len(word),[])+[word]

            
        
        

    def search(self, word):
        if len(word) not in self.dict:
            return False
        for cand in self.dict.get(len(word),[]):
            countdiff = 0
            for i in range(len(word)):
                if word[i] != cand[i]:
                    countdiff +=1
            if countdiff == 1:
                return True
        return False
            
        

        


# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dict)
# param_2 = obj.search(word)
