
class Node:
    def __init__(self,character):
        self.kids = dict()
        self.char = character
        self.isFinished = False
    

class Trie(object):

    def __init__(self):
        self.root = Node(None)
        

    def insert(self, word):
        i = 0
        cur = self.root
        while i < len(word):
            c = word[i]
            if c not in cur.kids:
                n = Node(c)
                cur.kids[c] = n
            i+=1
            cur = cur.kids[c]
        cur.isFinished = True
            
            
        

    def search(self, word):
        i = 0
        cur = self.root
        while i < len(word) and cur is not None:
            c = word[i]
            if c not in cur.kids:
                return False
            i+=1
            cur = cur.kids[c]
        if cur is None:
            return False
        return cur.isFinished

    def startsWith(self, word):
        i = 0
        cur = self.root
        while i < len(word):
            c = word[i]
            if c not in cur.kids:
                return False
            i+=1
            cur = cur.kids[c]
        if cur is None:
            return False
        return True

        

    def printTrie(self):
        print(self.root.kids['h'].kids['e'].kids['l'].kids['l'].kids['o'].isFinished)
        


# Your Trie object will be instantiated and called as such:
obj = Trie()
obj.insert("abc")
print(obj.search("abc"))
print(obj.startsWith("abcd"))
