class Solution:
    # @param S, a string
    # @param L, a list of string
    # @return a list of integer
    def findSubstring(self, S, L):
        res = []            # result list
        num = len(L)        # length of the str list 
        ls = len(S)
        if num == 0:
            return []
        str_len = len(L[0]) # length of each str
        #create the map: count the occurrance of each string
        #Note that set(L) is used to reduce the time, otherwise will not pass the large test
        map_str = dict((x,L.count(x)) for x in set(L))
        i = 0
        while i + num * str_len - 1 < ls:
            map_str2 = {}
            j = 0
            while j < num:
                subs = S[i + j * str_len:i + j * str_len + str_len ]
                if not subs in map_str:
                    break
                else:
                    # Note that dict.get(key, default_val) is used to handel the case that key NOT exist
                    map_str2[subs] = map_str2.get(subs, 0) + 1
                    if map_str2[subs]>map_str[subs]:
                        break
                    j = j + 1
            if j == num:
                res.append(i)
            i = i + 1
         
        return res
