

def removeDuplicates(array,n):
    track=0
    # finding and replace values in start...
    for i in range(n):
        if array[track]!=array[i] :
            track+=1
            array[track]=array[i]
    # also must to remove extra numbers...
    for i in range(n-track-1):
        array.pop()
    return 

