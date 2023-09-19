

# way-1
def removeDuplicates(array,n):
    temp=list()
    # store data after remove duplicates
    temp.append(array[0])
    for value in array[1:]:
        if(value!=temp[-1]):
            temp.append(value)
    # add-back your data on original array
    nn=len(temp)
    for i in range(n):
        array[i] = 0 if(i>=nn) else temp[i]
    return temp


# way-2
def removeDuplicates(array,n):
    temp=list()
    # store data after remove duplicates
    for value in array:
        if(temp==list() or value!=temp[-1]):
            temp.append(value)
    # add-back your data on original array
    nn=len(temp)
    for i in range(n):
        array[i] = 0 if(i>=nn) else temp[i]
    return temp

