
def secondLargest(anIntList):
    " return second largest int"

    # localCopy is a local variable
    # I can sort it, without affect anIntList
    localCopy = anIntList[:]
    localCopy.sort()    
    return localCopy[-2]

def test_secondLargest_1():
    assert secondLargest([3,7,2,9,1])==7

def test_secondLargest_2():
    assert secondLargest([4,10,2,6])==6
