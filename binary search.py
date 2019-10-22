# The following program is the solution to the Binary Search Practice quiz of the Data Structures & Algorithms class by Grow with Google/Udacity

def binary_search(input_array, value):
    """Your code goes here."""
    low_index = 0
    high_index = len(input_array) - 1
    
    while low_index <= high_index:
        mid_index = int((low_index + high_index)/2)
        if value == input_array[mid_index]:
            return mid_index
        elif value < input_array[mid_index]:
            high_index = mid_index - 1
        else:
            low_index = mid_index + 1
    return -1
            

test_list = [1,3,9,11,15,19,29]
test_val1 = 25
test_val2 = 15
print(binary_search(test_list, test_val1))
print(binary_search(test_list, test_val2))
