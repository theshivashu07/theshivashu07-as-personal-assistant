

#User function Template for python3
class Solution:
    def sort012(self,array,n):
        low,mid,high = 0,0,n-1
        # iterate till all the elements are sorted
        while mid<=high:
            # If the element is 0
            if array[mid]==0:
                array[low],array[mid] = array[mid],array[low]
                low = low+1
                mid = mid+1
            # If the element is 1
            elif array[mid]==1:
                mid = mid+1
            # If the element is 2
            else:
                array[mid],array[high] = array[high],array[mid]
                high = high-1
        return array

