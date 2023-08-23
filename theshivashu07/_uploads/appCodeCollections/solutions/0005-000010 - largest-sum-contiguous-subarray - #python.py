
#User function Template for python3
class Solution:

    #way-1: Function to find the sum of contiguous subarray with maximum sum.
    def maxSubArraySum(self,array,n):
        maxSum=array[0];
        currSum=0;
        for i in range(n): 
            currSum+=array[i];
            # if maxSum value less then currSum, update it...
            if(maxSum<currSum):
                maxSum=currSum;
            # if currSum goes less then 0, update it too...
            if(currSum<0):
                currSum=0;
        return maxSum;

    #way-2: Function to find the sum of contiguous subarray with maximum sum.
    def maxSubArraySum(self,array,n):
        maxSum=array[0];
        currSum=0;
        for i in range(n): 
            currSum+=array[i];
            # we want max, so below it take automatically...
            maxSum = max(maxSum,currSum)
            currSum = max(currSum,0)
        return maxSum;
