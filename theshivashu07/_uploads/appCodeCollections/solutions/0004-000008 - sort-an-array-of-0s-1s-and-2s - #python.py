

#User function Template for python3
class Solution:
    def sort012(self,array,n):
        left,right = 0,n-1
        index = 0
        while index<n and index<=right:
            # current element is 0
            if array[index] == 0:
                array[left],array[index] = array[index],array[left]
                left+=1; index+=1; 
            # current element is 2
            elif array[index] == 2:
                array[index],array[right] = array[right],array[index]
                right -= 1
            # current element is 1
            else:
                index += 1
        return array

