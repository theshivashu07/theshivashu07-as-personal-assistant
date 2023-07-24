

#User function Template for python3
class Solution:
    ##Complete this function
    #Function to find the sum of contiguous subarray with maximum sum.
    def maxSubArraySum(self,array,N):
        ##Your code here
        maxSum=array[0];
        currSum=0;
        for i in range(N): 
            currSum+=array[i];
            maxSum = max(maxSum,currSum)
            currSum = max(currSum,0)
        return maxSum;

