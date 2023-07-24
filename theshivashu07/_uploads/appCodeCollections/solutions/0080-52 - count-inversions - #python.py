

#User function Template for python3
class Solution:
    #Function to count inversions in the array.
    def inversionCount(self, array, n):
        # Your Code Here
        return self.mergeSort(array, 0, n-1);

    def mergeSort(self, array, left, right):
        invCount=0
        if(right>left):
            mid = (right+left) // 2
            invCount += self.mergeSort(array, left, mid)
            invCount += self.mergeSort(array, mid+1, right)
            invCount += self.merge(array, left, mid+1, right)
        return invCount;
        
    def merge(self, array, left, mid, right):
        i,j,k=left,mid,0;
        invCount=0
        temp = [0 for x in range(right-left+1)] 
        while(i<mid and j<=right):
            if(array[i]<=array[j]):
                temp[k]=array[i]
                k,i=k+1,i+1;
            else:
                temp[k]=array[j]
                invCount+=mid-i
                k,j=k+1,j+1; 
        while(i<mid):
            temp[k]=array[i]
            k,i=k+1,i+1; 
        while(j<=right):
            temp[k]=array[j]
            k,j=k+1,j+1; 
        k=0
        for i in range(left,right+1):
            array[i]=temp[k]
            k+=1            
        return invCount;

