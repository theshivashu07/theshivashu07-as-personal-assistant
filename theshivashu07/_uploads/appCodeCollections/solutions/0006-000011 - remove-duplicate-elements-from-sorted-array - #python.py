

# way-1
def removeDuplicates(array,n):
    temp=list()
    temp.append(array[0])
    for value in array[1:]:
        if(value!=temp[-1]):
            temp.append(value)
    return temp


# way-2
def removeDuplicates(array,n):
    temp=list()
    for value in array:
        if(temp==list() or value!=temp[-1]):
            temp.append(value)
    return temp

