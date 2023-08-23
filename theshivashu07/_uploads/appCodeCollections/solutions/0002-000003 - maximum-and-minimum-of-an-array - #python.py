

class Solution:
    def findSum(self,array,n): 
        minimum = maximum = array[0]
        for value in array:
            minimum = min(minimum,value)
            maximum = max(maximum,value)
        return [minimum,maximum]

