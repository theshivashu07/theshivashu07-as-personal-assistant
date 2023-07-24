
#User function Template for python3
class Solution:
    def minJumps(self, array, n):
        #code here
        if(n<=1):
            return 0;
        if(array[0]==0):
            return -1;
        reach_max = array[0];
        steps = array[0];
        jumps = 1;
        i=1;
        for i in range(1,n):
            if(i==n-1):
                return jumps;
            reach_max = max(reach_max,i+array[i]);
            steps-=1;
            if(steps==0):
                jumps+=1;
                if(i>=reach_max):
                    return -1;
                steps = reach_max-i;
        return

