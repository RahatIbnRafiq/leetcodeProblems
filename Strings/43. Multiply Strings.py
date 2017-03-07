class Solution(object):
    def multiply(self, num1, num2):
        m = len(num1)
        n = len(num2)
        res = []
        for i in range(0,(m+n)):
            res.append(0)
        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                p1,p2 = i+j,i+j+1
                n1,n2 = int(num1[i]),int(num2[j])
                mul = n1*n2
                sum = mul+res[p2]
                res[p1]+=sum/10
                res[p2]=sum%10
        res = [str(x) for x in res]
        res = "".join(res)
        i = 0
        while i < len(res) and res[i] == '0':
            i+=1
        return res[i:] if len(res[i:]) > 0 else "0"
