# The following program is the solution to the Sorting Practice quizes of the Data Structures & Algorithms class by Grow with Google/Udacity

def quicksort(array,start,end):
    if start < end:
        pIndex = partition(array, start, end)
        quicksort(array,start,pIndex-1)
        quicksort(array,pIndex+1,end)
        
    

def partition(array, start, end):
    pivot = array[end]
    pIndex = start
    for i in range(start,end):
        if array[i] <= pivot:
            temp = array[i]
            array[i] = array[pIndex]
            array[pIndex] = temp
            pIndex = pIndex + 1
    temp2 = array[pIndex]
    array[pIndex] = array[end]
    array[end] = temp2
    return pIndex


test = [7,2,1,6,8,5,3,4]
test2 = [7,2,1,6,8,5,3,4]
#print(partition(test,0,len(test)-1))
print(quicksort(test,0,len(test)-1))
