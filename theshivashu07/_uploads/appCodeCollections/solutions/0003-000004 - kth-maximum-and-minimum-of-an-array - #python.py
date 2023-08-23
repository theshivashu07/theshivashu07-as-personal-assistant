

#User function Template for python3
class Solution:
    def kthSmallest(self, array, left, right, k):
        array.sort()
        minimum = array[k-1]
        maximum = array[right-k+1]
        return [minimum,maximum]

