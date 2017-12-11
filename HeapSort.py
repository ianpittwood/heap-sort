from random import *
import copy
import time

#Define constants for the different possible cases
BEST_CASE = 1
AVERAGE_CASE = 2
WORST_CASE = 3

#Function to randomize list each test
def randomizeList(case):
    lengthOfArray = 1
    #setup different cases of difficulty for the sort
    if (case == BEST_CASE):
        lengthOfArray = randint(1,500)
    elif (case == AVERAGE_CASE):
        lengthOfArray = randint(500,1000)
    elif (case == WORST_CASE):
        lengthOfArray = randint(1000,10000)

    newRandomArray = []
    #for best and average case just generate random ints b/t 0 and 1000
    if (case == BEST_CASE or case == AVERAGE_CASE):
        for i in range(lengthOfArray):
            newRandomArray.append(randint(0,1000))
    #for worst case make each number distinct and shuffle for maximum difficulty
    elif (case == WORST_CASE):
        for i in range(lengthOfArray):
            newRandomArray.append(i)
        shuffle(newRandomArray)

    return newRandomArray

def isHeap(arrayX):
    return all(arrayX[i] <= arrayX[(i-1)//2] for i in range(1, len(arrayX)))

def heapsort(arrayX):
    #find array length and parent/root node
    lengthOfArray = len(arrayX) - 1
    leastParent = int(round(lengthOfArray/2))

    #for all nodes less than the root move lower
    for i in range(leastParent, -1, -1):
        moveLower(arrayX, i, lengthOfArray)
    #invariant: a[1,n] in heap order
    assert(isHeap(arrayX))

    #for all nodes from lengthOfArray to 0s
    for i in range(lengthOfArray, 0, -1):
        #if the index 0 is greater than index i then swap 0 and i and moveLower on 0, i-1
        if arrayX[0] > arrayX[i]:
            swap(arrayX, 0, i)
            moveLower(arrayX, 0, i-1)
            #invariant: a[n-i+1:n] sorted

    return

def moveLower(arrayX, first, last):
    largest = 2*first + 1
    while largest <= last:
        if (largest < last) and (arrayX[largest] < arrayX[largest+1]):
            largest+=1;
        if (arrayX[largest] > arrayX[first]):
            swap(arrayX, largest, first)
            first = largest
            largest = 2*first + 1
        else:
            return

def swap(A, x, y):
    tmp = A[x]
    A[x] = A[y]
    A[y] = tmp

def main(case):
    arr = randomizeList(case)
    sortedArray = copy.deepcopy(arr)
    start_time = time.time()
    heapsort(sortedArray)
    #invariant: every index i is >= index i-1
    for i in range(1,len(sortedArray)):
        assert(sortedArray[i] >= sortedArray[i-1])
    print("Heapsort was successful.")
    return (time.time() - start_time)

timeForBestCase = main(BEST_CASE)
timeForAverageCase = main(AVERAGE_CASE)
timeForWorstCase = main(WORST_CASE)

print("The execution time for the best case was " + str(timeForBestCase) + "s")
print("The execution time for the average case was " + str(timeForAverageCase) + "s")
print("The execution time for the worst case was " + str(timeForWorstCase) + "s")
