class Solution(object):
    def minWindow(self, s, t):
        from collections import Counter
        c = Counter(t)
        start,end = 0,0
        min_window_length = len(s)+1
        min_window_start = 0
        num_chars_needed= len(t)
        
        while end < len(s):
            if s[end] in c:
                if c[s[end]] > 0:
                    num_chars_needed -= 1
                c[s[end]] -= 1
            while num_chars_needed == 0:
                if end-start+1 < min_window_length:
                    min_window_length = end-start+1
                    min_window_start = start
                if s[start] in c:
                    c[s[start]]+=1
                    if c[s[start]] > 0:
                        num_chars_needed+=1
                start+=1
            end+=1
        if min_window_length == len(s)+1:return ""
        return s[min_window_start:min_window_start+min_window_length]
                    
                    
            
            
        
