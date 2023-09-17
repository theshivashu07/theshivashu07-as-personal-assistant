

def getLargestElementIndex(array,n):
    temp=array[0]
    for i in range(n):
        if temp<array[i]:
            temp=array[i]
    return temp

def getLargestElementIndex(array,n):
    temp=array[0]
    for i in range(n):
        temp=max(temp,array[i])
    return temp
    
