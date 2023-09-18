

# way-1
def reverseList(array,n):
    start,end=0,n-1
    while start < end:
        array[start],array[end] = array[end],array[start]
        start += 1; end -= 1;
    return


# way-2
def reverseList(array,n):
    for i in range(n//2):
        array[i],array[n-i-1] = array[n-i-1],array[i]
    return
 

