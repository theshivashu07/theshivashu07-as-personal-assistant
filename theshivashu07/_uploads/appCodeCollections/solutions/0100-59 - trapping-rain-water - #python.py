class Solution:
    def trappingWater(self, array,n):
        #Code here
        stack = list() 
        result = 0
        for i in range(n):
            while(stack and (array[stack[-1]] < array[i])):  # (len(stack)!=0 and .....)
                pop_height = array[stack[-1]]
                stack.pop()
                if(not stack):  # if(len(stack)==0):
                    break
                distance = i - stack[-1] - 1
                min_height = min(array[stack[-1]], array[i])-pop_height
                result += distance * min_height
                #print("Under while : ",pop_height,distance,min_height,result)
            stack.append(i)
            #print("Final for : ",stack)
        return result
 
