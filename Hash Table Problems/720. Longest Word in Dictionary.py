class Solution(object):
    def longestWord(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        words.sort()
        candidates = []
        res = ""
        max_len = 0
        first_flag = True
        for item in words:
            if len(item) == 1:
                candidates.append(item)
                if first_flag:
                    res = item
                    max_len = 1
                    first_flag = False

            else: 
                if item[:-1] in candidates:
                    candidates.append(item)
                    if len(item) > max_len:
                        res = item
                        max_len = len(item)
        
        return res
