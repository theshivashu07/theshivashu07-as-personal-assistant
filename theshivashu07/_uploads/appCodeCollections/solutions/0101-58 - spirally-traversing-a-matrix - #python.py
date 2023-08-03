#User function Template for python3
class Solution:    
    #Function to return a list of integers denoting spiral traversal of matrix.
    def spirallyTraverse(self,matrix, r, c):         
        if not matrix or not matrix[0]:
            return list()
                    
        startRow,startColumn=0,0
        endRow,endColumn=r-1,c-1
        result=list()

        while(startRow<=endRow and startColumn<=endColumn):

            if(startRow<=endRow and startColumn<=endColumn):
                for updated in range(startColumn,endColumn+1): 
                    result.append(matrix[startRow][updated])
                startRow+=1

            if(startRow<=endRow and startColumn<=endColumn):
                for updated in range(startRow,endRow+1): 
                    result.append(matrix[updated][endColumn])
                endColumn-=1 

            if(startRow<=endRow and startColumn<=endColumn):
                for updated in range(endColumn,startColumn-1,-1): 
                    result.append(matrix[endRow][updated])
                endRow-=1 

            if(startRow<=endRow and startColumn<=endColumn):
                for updated in range(endRow,startRow-1,-1): 
                    result.append(matrix[updated][startColumn])
                startColumn+=1 

        return result

