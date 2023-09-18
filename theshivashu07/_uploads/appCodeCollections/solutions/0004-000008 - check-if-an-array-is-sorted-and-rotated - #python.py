

def checkRotatedAndSorted1(array, n):
    ''' Not Distinct/Unique  |  Rotated&Sorted Both Must !!! '''
    okay=nokay=0 
    # last with first place tracking is must, to check that is really this is Rotated or not?!!
    isLastNokay= True if array[n-1]<=array[0] else False 
    for i in range(n):
        if array[i]<=array[(i+1)%n]:
            okay+=1
        else:
            nokay+=1
    if(nokay==1 and isLastNokay):
        return True
    return False


def checkRotatedAndSorted2(array, n): 
    ''' Distinct/Unique Only  |  Rotated&Sorted Both Must !!! '''
    okay=nokay=0 
    # last with first place tracking is must, to check that is really this is Rotated or not?!!
    isLastNokay= True if array[n-1]<array[0] else False  # x<=y 
    for i in range(n):
        if array[i]<array[(i+1)%n]:  # x<=y 
            okay+=1
        else:
            nokay+=1
    if nokay==1 and isLastNokay:
        return True
    return False


def checkRotatedAndSorted3(array, n):
    ''' Not Distinct/Unique  |  Sorted or Rotated&Sorted !!! '''
    okay=nokay=0 
    for i in range(n):
        if array[i]<=array[(i+1)%n]:
            okay+=1
        else:
            nokay+=1
    if nokay==1:
        return True
    return False


def checkRotatedAndSorted4(array, n): 
    ''' Distinct/Unique Only  |  Sorted or Rotated&Sorted !!! '''
    okay=nokay=0 
    for i in range(n):
        if array[i]<array[(i+1)%n]:
            okay+=1
        else:
            nokay+=1
    if nokay==1:
        return True
    return False

