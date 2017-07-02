#Everett Williams
#30JUN17 as of 02JUL17
#HW1 Problem 4
#Insert sort program

#sort array using insertion sort algorithm
def insertionSort(array):
    for j in range(2, array[0] + 1):
        key = array[j]
        i = j - 1
        while i > 0 and array[i] > key:
            array[i + 1] = array[i]
            i -= 1
        array[i + 1] = key
    del array[0]
    return array


#read data from data.txt and store data as integers into the list dataArray and
#return unsorted array
def readArray():
    with open('data.txt') as data:
        dataArray = []
        for line in data:
            line = line.split() # to deal with blank
            if line:            # lines (ie skip them)
                for value in line:
                    num = int(value)
                    dataArray.append(num)
    return dataArray

#write sorted array to insert.out
def outPutArray(array):
    with open('insert.out', 'w') as outPutFile:
        for val in array:
            num = str(val)
            outPutFile.write(num + " ")

#Main program
unsortedArray = readArray()
sortedArray = insertionSort(unsortedArray)
print(sortedArray)
outPutArray(sortedArray)
