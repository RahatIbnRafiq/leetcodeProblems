class Solution(object):
    def dailyTemperatures(self, temps):
        stack = []
        result = [0 for t in temps]
        for i in range(0,len(temps)):
            while len(stack) > 0 and temps[i] > temps[stack[-1]]:
                idx = stack.pop()
                result[idx] = i-idx
            stack.append(i)
        return result
        
