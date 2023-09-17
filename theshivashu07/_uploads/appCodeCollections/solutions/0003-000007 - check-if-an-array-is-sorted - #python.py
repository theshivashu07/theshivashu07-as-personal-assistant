

def arraySortedOrNot(array, n):
    for i in range(n-1):
        if(array[i]>array[i+1]):
            return False
    return True

