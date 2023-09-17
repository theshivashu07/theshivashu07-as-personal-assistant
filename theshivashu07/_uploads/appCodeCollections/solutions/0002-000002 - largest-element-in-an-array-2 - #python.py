

def getLargestElement(array,n):
    for i in range(n):
        flag=True
        for j in range(n):
            if array[i]<array[j]:
                flag=False
                break
        if flag:
            return array[i]
    # never coming place
    return -1

def getLargestElement(array,n):
    for i in range(n):
        flag=True
        for j in range(n):
            if array[i]<array[j]:
                break
        else:
            return array[i]
    # never coming place
    return -1

