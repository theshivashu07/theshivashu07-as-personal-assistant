

def getLargestElementIndex(array,n):
    for i in range(n):
        flag=True
        for j in range(n):
            if array[i]<array[j]:
                flag=False
                break
        if flag:
            return i+1
    # never coming place
    return -1

def getLargestElementIndex(array,n):
    for i in range(n):
        flag=True
        for j in range(n):
            if array[i]<array[j]:
                break
        else:
            return i+1
    # never coming place
    return -1

