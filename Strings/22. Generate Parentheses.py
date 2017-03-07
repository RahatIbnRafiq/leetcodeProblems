class Solution(object):
    def generateParenthesis(self, n):
        self.result = []
        self.helper(n,n,"")
        return self.result

    def helper(self,left,right,path):
        if left < 0 or right < 0: return
        if left > right:return
        if left == 0 and right == 0:
            self.result.append(path)
            return
        else:
            self.helper(left-1,right,path+"(")
            self.helper(left,right-1,path+")")
