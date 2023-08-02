#User function Template for python3
class Solution:
    #Function to find if there is a celebrity in the party or not.
    def celebrity(self, data, n):
        # code here
        # Here c stads for Celebrity...
        c=0;
        for i in range(1,n):
            if(data[c][i]==1):
                    c=i;
        for i in range(n):
            if(i!=c and (data[c][i]==1 or data[i][c]==0)):
                return -1;
        return c;

