
import heapq
def solution(A):
    """h = []
    first,last = 0,len(A)-1
    heapq.heappush(h,A[0])
    for i in range(1,len(A)):
        temp = heapq.nlargest(1,h)[0]
        if A[i] < temp:
            first = i-1
            break
        else:heapq.heappush(h,A[i])
    


    h = []
    heapq.heappush(h,A[-1])
    for i in range(len(A)-2,-1,-1):
        temp = heapq.nsmallest(1,h)[0]
        if A[i] > temp or A[i] < A[first]:
            last = i
            break
        else:
            heapq.heappush(h,A[i])
    return (last-first+1)"""
    
        
    
    




print solution([1,2,6,5,5,8,9])
