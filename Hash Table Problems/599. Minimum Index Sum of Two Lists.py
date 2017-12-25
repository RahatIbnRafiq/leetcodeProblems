class Solution(object):
    def findRestaurant(self, list1, list2):
        m1 = dict()
        for i in range(0,len(list1)):
            m1[list1[i]] = i
        
        
        m2 = dict()
        for i in range(0,len(list2)):
            m2[list2[i]] = i
        
        res = 30000
        rest = []
        for key in m1.keys():
            if key in m2:
                if res > m1[key]+m2[key]:
                    res = m1[key]+m2[key]
                    rest =[key]
                elif res == m1[key]+m2[key]:
                    rest.append(key)
        return rest
                
