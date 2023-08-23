#User function Template for python3
class Solution:

    # approach-1
    def sort012(self,array,n):
        tracks = dict()
        for value in array:
            tracks[value]=tracks.get(value,0)+1
        get=0  # 012's-positioning-tracking...
        for i in range(n):
            array[i] = get  # assignment is there
            tracks[get] = tracks.get(get)-1  #update
            if(tracks[get]==0): # check-up
                get+=1
        return array

    # approach-2
    def sort012(self,array,n):
        tracks = [0,0,0]
        for value in array:
            tracks[value] += 1
        index=0  # this is tracks indexings...
        for i in range(len(tracks )):
            for j in range(tracks[i]):
                array[index]=i
                index+=1

    # approach-3
    def sort012(self,array,n):
        zeros = once = twice = 0
        tracks = [0,0,0]
        for value in array:
            if(value==0):
                zeros+=1
            elif(value==1):
                once+=1
            elif(value==2):
                twice+=1
        for i in range(n):
            if(zeros):
                get=0; zeros-=1
            elif(once):
                get=1; once-=1
            elif(twice):
                get=2; twice-=1
            array[i] = get
        return array

