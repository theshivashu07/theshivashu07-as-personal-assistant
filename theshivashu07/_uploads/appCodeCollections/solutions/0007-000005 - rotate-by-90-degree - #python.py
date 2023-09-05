

#User function Template for python3
class Solution:
    #Function to rotate matrix anticlockwise by 90 degrees.
    def rotateby90(self, array, N):
        # code here
        # "Transpose of Matrix" problem's logic.....
        for i in range(N):
            for j in range(i+1,N):
                array[i][j],array[j][i]=array[j][i],array[i][j];
        # NEW logic to "Reverse Individual Columns".....
        for i in range(N):
            low=0; high=N-1;
            while(low<high):
                array[low][i],array[high][i]=array[high][i],array[low][i];
                low+=1; high-=1;
        return;

