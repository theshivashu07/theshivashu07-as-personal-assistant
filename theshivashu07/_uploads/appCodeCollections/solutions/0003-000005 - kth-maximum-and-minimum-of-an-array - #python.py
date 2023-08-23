

import heapq
#User function Template for python3
class Solution:
    def kthSmallest(self, array, left, right, k):
        maxheap,minheap = list(),list()
        for value in array:
            heapq.heappush(maxheap,value)
            heapq.heappush(minheap,-1*value)
            if(len(maxheap)>k):
                heapq.heappop(maxheap)
            if(len(minheap)>k):
                heapq.heappop(minheap)
        maximum = heapq.heappop(maxheap)
        minimum = -1*heapq.heappop(minheap)
        return [minimum,maximum]

