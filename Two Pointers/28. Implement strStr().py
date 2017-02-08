class Solution(object):
    
    def strStr(self, haystack, needle):
        if len(needle) == 0: return 0
        if len(haystack) < len(needle):return -1
        if len(haystack) == 0 and len(needle) == 0: return 0
        self.array = [0 for i in range(0,len(needle))]
        for i in range(1,len(needle)):
            j = self.array[i-1]
            while j> 0 and needle[i]!=needle[j]:
                j = self.array[j-1]
            if needle[i] == needle[j]: self.array[i] = j+1
            else:self.array[i] = j

        ret = []
        j = 0

        for i in range(len(haystack)):
            while j > 0 and haystack[i] != needle[j]:
                j = self.array[j - 1]
            if haystack[i] == needle[j]:
                j+=1
            if j == len(needle):
                return i-(j - 1)
        return -1
