def binarySearch(myList, value):
    lowerBound = 0
    upperBound = len(myList) - 1

    while lowerBound <= upperBound:
        midIndex = (lowerBound + upperBound) // 2
        if myList[midIndex] == value:
            return midIndex
        else:
            if value < myList[midIndex]:
                upperBound = midIndex - 1
            else:
                lowerBound = midIndex + 1
    

# List needs to be sorted
myList = [2,7,19,34,53,72]

print(binarySearch(myList, 7))
print(binarySearch(myList, 78))
