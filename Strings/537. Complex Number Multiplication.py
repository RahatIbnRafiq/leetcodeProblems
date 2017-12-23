class Solution(object):
    def complexNumberMultiply(self, a, b):
        tokens1 = a.split("+")
        a1 = int(tokens1[0])
        b1 = int(tokens1[1][0:len(tokens1[1])-1])
        
        tokens2 = b.split("+")
        a2 = int(tokens2[0])
        b2 = int(tokens2[1][0:len(tokens2[1])-1])
        
        a3 = (a1*a2)-(b1*b2)
        
        b3 =(a1*b2+b1*a2)
        return str(a3)+"+"+str(b3)+"i"
        
