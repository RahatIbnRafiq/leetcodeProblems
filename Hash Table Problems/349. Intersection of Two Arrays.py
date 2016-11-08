class Solution(object):
    def intersection(self, nums1, nums2):
        n1,n2 = dict(),dict()
        for n in nums1: n1[n] = n1.get(n,0)+1
        for n in nums2: n2[n] = n2.get(n,0)+1
        
        res  = []
        for key in n1.keys():
            if key in n2: res.append(key)
        return res
                
