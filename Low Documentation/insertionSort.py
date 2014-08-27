sortedUpTil = 0
toSort = [-1, 3,1,6,1,9,-4,7]
print(toSort)
while sortedUpTil < len(toSort) and sortedUpTil < len(toSort) - 1:
    print("w")
    if toSort[sortedUpTil + 1]  >= toSort[sortedUpTil]:
        print("i")
        sortedUpTil += 1
    else:
        print("e")
        # find the element in the sorted section that is less than current element
        # or the end of the list. Then move all the elements that were passed over up
        # 1 index to make room.
        tsVal = toSort[sortedUpTil + 1] 
        i = sortedUpTil
        while i >= 0 and toSort[i] > tsVal:
            print("ew")
            toSort[i + 1] = toSort[i]
            i = i - 1;
            print(toSort)
        else:
            print("ewe")
            toSort[i + 1] = tsVal
            print(toSort)
    print(toSort)
else:
    print(toSort)
