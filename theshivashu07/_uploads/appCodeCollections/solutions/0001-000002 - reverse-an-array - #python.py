

def reverse(array):
        n=len(array)
        for i in range(n//2):
                array[i],array[n-i-1] = array[n-i-1],array[i]
        return array

