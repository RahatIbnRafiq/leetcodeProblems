import collections
class WordDictionary(object):

    def __init__(self):
        self.word_dict = collections.defaultdict(list)
        

    def addWord(self, word):
        if word:
            self.word_dict[len(word)].append(word)
        

    def search(self, word):
        if not word:
            return False
        if '.' not in word:
            return word in self.word_dict[len(word)]
        for cand in self.word_dict[len(word)]:
            k = 0
            for i, ch in enumerate(word):
                if cand[i] != ch and ch != ".":
                    break
                k+=1
            if k == len(word):
                return True
        return False
