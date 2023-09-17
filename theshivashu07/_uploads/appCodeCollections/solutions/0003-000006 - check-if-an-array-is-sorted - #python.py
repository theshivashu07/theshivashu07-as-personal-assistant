
def arraySortedOrNot(array, n):
    if n==1 or n==0:
        return True
    return array[0]<=array[1] and arraySortedOrNot(array[1:])
    #return array[n-1]>=array[n-2] and arraySortedOrNot(array,n-1)

