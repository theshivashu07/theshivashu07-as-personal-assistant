
def reverse(array,n):
        newarray=list()
        for i in range(n):
                newarray[n-i-1]=array[i]
        return newarray

