

# way-1
def reverseList(array,n):
    start,end=0,n-1
    reverseFunc(array,start,end)
    return 

def reverseFunc(array, start, end):
    if start >= end:
        return
    array[start],array[end] = array[end],array[start]
    return reverseFunc(array, start+1, end-1)


# way-2
def reverseList(array,n,start=None,end=None):
    # special-case
    if(start==None and end==None):
        start,end = 0,n-1
    # original-code 
    if start < end:
        array[start],array[end] = array[end],array[start]
        reverseList(array, n, start+1, end-1)
    return

