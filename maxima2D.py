import copy


def mergeSort(arr, key):
    sortCount = 0

    if len(arr) > 1:
        mid = len(arr)//2  # Finding the mid of the array
        L = arr[:mid]  # Dividing the array elements
        R = arr[mid:]  # into 2 halves

        sortCount += mergeSort(L, key)  # Sorting the first half
        sortCount += mergeSort(R, key)  # Sorting the second half

        i = j = k = 0

        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i][key] < R[j][key]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
            sortCount += 1

        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

    return sortCount


def groupingPointList(output, pointListNumber):
    """
    This function is for taking all the lines from our file and then grouping the ones
    that belong together.
    """
    i = 0
    points = []
    pointValue = int(output[0])
    del output[0]

    for x in range(pointValue):

        if i != pointValue:
            points.append({'Point List Number': pointListNumber,
                           'Point Amount': pointValue,
                           'x': float(output[x].split()[0]),
                           'y': float(output[x].split()[1]),
                           'Maximal': False,
                           'Where': i + 1})
            i += 1

    del output[0:pointValue]

    return points, output


def getMaxima(pointList):
    x = 1
    currentMaxima = pointList[0]
    maximaList = []
    maximaList.append(currentMaxima)

    while(x != len(pointList)):
        if pointList[x]['x'] > currentMaxima['x']:
            currentMaxima['maximal'] = False
            pointList[x]['maximal'] = True
            currentMaxima = pointList[x]
            maximaList.append(currentMaxima)

        elif pointList[x]['x'] == currentMaxima['x']:
            if pointList[x]['y'] >= currentMaxima['y']:
                currentMaxima['maximal'] = False
                pointList[x]['maximal'] = True
                currentMaxima = pointList[x]
                maximaList.append(currentMaxima)
        x += 1

    return {'MaxCtA': x - 1,
            'maxNumA': len(maximaList),
            'Maximal Order': maximaList}


def printResults(pointList, maximaList, sortCountList):
    for x in range(len(pointList)):
        print("Output for the " + str(x) + "-th Set of Points")
        print("=================================")
        print("Input Size = " + str(pointList[x][1]['Point Amount']))
        print("sortCount = " + str(sortCountList[x]))
        print("maxCountA = " + str(maximaList[x]['MaxCtA']))
        print("maxNumA = " + str(maximaList[x]['maxNumA']))

        print("\nMaxima(S): (where: x, y)")
        print("---------------------------")
        for y in range(len(maximaList[x]['Maximal Order'])):
            print(str(maximaList[x]['Maximal Order'][y]['Where']) + ": (" +
                  str(maximaList[x]['Maximal Order'][y]['x']) + ", " +
                  str(maximaList[x]['Maximal Order'][y]['y']) + ")")

        print("\n=========================================\n")

    print("\n" + "Statistics for the " + str(len(sortCountList)) + " iterations:")
    print("\nIter SortCt  MaxCtA SortCt+MaxCtA")
    print("--------------------------------------------------")
    for z in range(len(pointList)):
        print("  " + str(z) + "   " + str(sortCountList[z]) + "    " +
              str(maximaList[z]['MaxCtA']) + "       " +
              str(sortCountList[z] + maximaList[z]['MaxCtA']))
    print("\n")


if __name__ == '__main__':
    filename = 'points1.txt'
    output = []
    pointListX = []
    pointListY = []
    sortCountList = []
    maximaList = []
    lock = True
    x = 0
    pointGroupCounter = 0

    with open(filename, 'r') as f:
        for line in f:
            output.append(line.strip())

    while(lock):
        if output:
            points, output = groupingPointList(output, pointGroupCounter)
            pointListX.append(copy.deepcopy(points))
            pointGroupCounter += 1
        else:
            lock = False

    pointListY = copy.deepcopy(pointListX)

    while(x != len(pointListX)):
        sortCountList.append(mergeSort(pointListX[x], 'x'))
        mergeSort(pointListY[x], 'y')
        x += 1

    x = 0
    while(x != len(pointListY)):
        pointListY[x].reverse()
        maximaList.append(getMaxima(pointListY[x]))
        x += 1

    printResults(pointListX, maximaList, sortCountList)
