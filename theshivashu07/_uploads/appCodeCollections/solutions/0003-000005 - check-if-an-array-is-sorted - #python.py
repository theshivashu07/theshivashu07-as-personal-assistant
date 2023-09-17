

def arraySortedOrNot(array, n):
    for i in range(n):
        for j in range(i+1,n):
            if(array[i]>array[j]):
                return False
    return True

