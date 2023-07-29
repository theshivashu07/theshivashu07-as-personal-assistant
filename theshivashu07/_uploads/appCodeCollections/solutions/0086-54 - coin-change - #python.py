

#User function Template for python3
class Solution:
    # code here
    def __init__(self):
        self.dp=[[ i for i in range(1000) ] for i in range(1000)];

    def count(self, array, m, n):
        for i in range(m):
            for j in range(n+1):
                self.dp[i][j]=-1;
        return self.solve(array,m-1,n);
        
    def solve(self,array,m,n):
        # because if our m is empty but n is not, means its not a valid...
        if(m==-1 and n>0):
            return 0;
        # if n==0 means its a valid, thats why we return 1!
        if(n==0):
            return 1;
        # suppose our value is going negative side, then return 0!
        if(n<0):
            return 0;
        # means memorilization heppens, same things come again...
        data=self.dp[m][n]
        if(data!=-1):
            return data;

        # now we again call this function as recursion's form,
        # first's minus sum not index, and second's minus index not sum
        self.dp[m][n] = self.solve(array,m,n-array[m]) + self.solve(array,m-1,n);
        return self.dp[m][n];

