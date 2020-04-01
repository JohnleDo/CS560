def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr)//2  # Finding the mid of the array
        L = arr[:mid]  # Dividing the array elements
        R = arr[mid:]  # into 2 halves

        mergeSort(L)  # Sorting the first half
        mergeSort(R)  # Sorting the second half

        i = j = k = 0

        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1


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
                           'x': output[x].split()[0],
                           'y': output[x].split()[1],
                           'maximal': False,
                           'where': i})
            i += 1

    del output[0:pointValue]

    return points, output


if __name__ == '__main__':
    filename = 'points1.txt'
    output = []
    pointList = []
    lock = True
    pointGroupCounter = 0

    with open(filename, 'r') as f:
        for line in f:
            output.append(line.strip())

    while(lock):
        if output:
            points, output = groupingPointList(output, pointGroupCounter)
            pointList.append(points.copy())
            pointGroupCounter += 1
        else:
            lock = False
