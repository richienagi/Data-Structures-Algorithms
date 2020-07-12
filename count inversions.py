# Count inversions in a list. The inversions.txt contains the list of numbers

my_file = open("inversionstxt.txt", "r")
content_list = my_file.read().split()

test = []

for i in range(0,len(content_list)):
    test.append(int(content_list[i]))  

def sort_and_count_Inv(inputArray):
    if len(inputArray) <= 1:
        return inputArray,0
    else:
        midIndex = len(inputArray)//2
        leftArray,leftInv = sort_and_count_Inv(inputArray[:midIndex])
        rightArray,rightInv = sort_and_count_Inv(inputArray[midIndex:])
        
        i = j = k = splitInv = 0
        
        while i < len(leftArray) and j < len(rightArray):
            if leftArray[i] < rightArray[j]:
                inputArray[k] = leftArray[i]
                i = i + 1
            else:
                inputArray[k] = rightArray[j]
                j = j + 1
                splitInv = splitInv + (len(leftArray) - i)
            k = k + 1
            
        while i < len(leftArray):
            inputArray[k] = leftArray[i]
            i = i + 1
            k = k + 1
        
        while j < len(rightArray):
            inputArray[k]= rightArray[j]
            j = j + 1
            k = k + 1
        
        return inputArray,leftInv + rightInv + splitInv
        

x = sort_and_count_Inv(test)    
