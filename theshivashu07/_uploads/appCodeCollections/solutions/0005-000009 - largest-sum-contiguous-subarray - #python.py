

#User function Template for python3
class Solution:
    #Function to find the sum of contiguous subarray with maximum sum.
    def maxSubArraySum(self,array,n):
        maxSum=array[0];
        for i in range(n):
            currSum=0;
            for j in range(i,n):
                currSum += array[j]
                maxSum = max(currSum,maxSum)
        return maxSum;

