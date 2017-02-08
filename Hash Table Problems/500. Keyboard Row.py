class Solution(object):
    def findWords(self, words):
        self.dic = dict()
        l1 = ["q","w","e","r","t","y","u","i","o","p","Q","W","E","R","T","Y","U","I","O","P"]
        l2 = ["a","s","d","f","g","h","j","k","l","A","S","D","F","G","H","J","K","L"]
        l3 = ["z","x","c","v","b","b","n","m","Z","X","C","V","B","N","M"]
        if len(self.dic) == 0:
            for c in l1:
                self.dic[c] = 1
            for c in l2:
                self.dic[c] = 2
            for c in l3:
                self.dic[c] = 3
        result = []
        
        for word in words:
            isTrue = True
            pos = self.dic[word[0]]
            for char in word[1:]:
                if self.dic[char]!=pos:
                    isTrue = False
                    break
            if isTrue:
                result.append(word)
        return result
                
