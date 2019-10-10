"""You're going to write a binary search function.
You should use an iterative approach - meaning
using loops.
Your function should take two inputs:
a Python list to search through, and the value
you're searching for.
Assume the list only has distinct elements,
meaning there are no repeated values, and 
elements are in a strictly increasing order.
Return the index of value, or -1 if the value
doesn't exist in the list."""
import math
def binary_search(input_array, value):
    size = len(input_array)
    if size > 0:
        number_of_loops = int(round(math.sqrt(size)))
        print number_of_loops
        size = size/2 + 1
        index = size - 1
        for i in range(number_of_loops):
            print i, size, index
            if input_array[index] == value:
                return index
            size = size/2
            if input_array[index] > value:
                index = index - size
            else:
                index = index + size
    return -1

test_list = [1,3,9,11,15,19,29]
test_val1 = 25
test_val2 = 15
print binary_search(test_list, test_val1)
print binary_search(test_list, test_val2)
