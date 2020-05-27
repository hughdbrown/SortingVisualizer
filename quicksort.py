import time

max_time = 0.250
swapCount = 0

def quickSort(arr, displayArray, speedInput, pauseBool):
    global swapCount
    swapCount = 0
    low, high = 0, len(arr) - 1
    _quick_sort(arr, displayArray, speedInput, pauseBool, low, high)

def _quick_sort(arr, displayArray, speedInput, pauseBool, low, high):
    if low < high:
        #--partition index
        partInd = _partition(arr, displayArray, speedInput, pauseBool, low, high)

        _quick_sort(arr, displayArray, speedInput, pauseBool, low, partInd-1)
        _quick_sort(arr, displayArray, speedInput, pauseBool, partInd+1, high)



##--taking last element as pivot
##--separates smaller elements to the left and larger to the right
def _partition(arr, displayArray, speedInput, pauseBool, low, high):
    global swapCount

    pointer = low
    pivot = arr[high]

    displayArray(arr, generateColorArray(low, high, pointer, pointer, len(arr), False), swapCount)
    time.sleep(max_time - (speedInput * max_time / 100))

    for j in range(low, high):

        if arr[j] < pivot:
            displayArray(arr, generateColorArray(low, high, pointer, j, len(arr), True), swapCount)
            time.sleep(max_time - (speedInput * max_time / 100))

            arr[j], arr[pointer] = arr[pointer], arr[j]
            pointer += 1
            swapCount += 1

        displayArray(arr, generateColorArray(low, high, pointer, j, len(arr), False), swapCount)
        time.sleep(max_time - (speedInput * max_time / 100))

    displayArray(arr, generateColorArray(low, high, pointer, high, len(arr), False), swapCount)
    time.sleep(max_time - (speedInput * max_time / 100))

    arr[high], arr[pointer] = arr[pointer], arr[high]
    swapCount += 1

    colorArray = ['green'] * len(arr)
    displayArray(arr, colorArray, swapCount)

    return pointer


def generateColorArray(low, high, pointer, curr_ind, n, swapping):
    colorArray = []

    for i in range(n):
        if low <= i <= high:
            colorArray.append('yellow')##our range
        else:
            colorArray.append('#996633')##general

        if i == pointer:
            colorArray[i] = 'black'##pointer
        elif i == high:
            colorArray[i] = 'red'##pivot
        elif i == curr_ind:
            colorArray[i] = 'blue'

        if swapping:
            if i == curr_ind or i == pointer:
                colorArray[i] = 'green'
    return colorArray
