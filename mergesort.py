#Everett Williams
#30JUN17 as of 02JUL17
#HW1 Problem 4
#Merge sort program

#sort array using merge sort algorithm
def mergeSort(alist):
    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)  #returns sorted left half which is sorted with the below while statements
        mergeSort(righthalf)  #returns sorted right half which is sorted with the below while statements
        merge(lefthalf, righthalf, alist)
        return alist

#helper function to merge sub arrays
def merge(lefthalf, righthalf, blist):
        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf): #while both arrays lt length compare values
            if lefthalf[i] < righthalf[j]:
                blist[k]=lefthalf[i]
                i=i+1
            else:
                blist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):  #when rt array has nothing left to check append remaining left elements
            blist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf): ##when lt array has nothing left to check append remaining right elements
            blist[k]=righthalf[j]
            j=j+1
            k=k+1


#read data from data.txt and store data as integers into the list dataArray and
#return unsorted array
def readArray():
    with open('data.txt') as data:
        for line in data:
            dataArray = []
            line = line.split() # to deal with blank
            if line:            # lines (ie skip them)
                for value in line:
                    num = int(value)
                    dataArray.append(num)
            del dataArray[0]
            sortedArray = mergeSort(dataArray)
            outPutArray(sortedArray)
    return dataArray

#write sorted array to merge.out
def outPutArray(array):
    with open('merge.out', 'a') as outPutFile:
        for val in array:
            num = str(val)
            outPutFile.write(num + " ")
        outPutFile.write("\n")


#Main program
readArray()
