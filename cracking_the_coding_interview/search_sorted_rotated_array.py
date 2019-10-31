'''
Search in Rotated Array:

Given a sorted array of n integers that has been rotated an unknown
number of times, write code to find an element in the array.
You may assume that the array was originally sorted in increasing order.

EXAMPLE
input: find 5 in {15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14}
output: 8 (the index of 5 in the array) 

Hints
# 298: Can you modify Binary Search for this? 
# 310: What if the array has duplicates?
'''
# Solution works for Duplicates too
def search_sorted_rotated(arr, key):
    return search(arr, 0, len(arr) - 1, key)

def search(arr, low, high, key):
    if low > high:
        return -1
    mid = (low + high) // 2
    if arr[mid] == key:
        return mid
    # left part is sorted
    if arr[low] < arr[mid]:
        # key is in left sorted array
        if arr[low] <= key and arr[mid] > key:
            return search(arr, low, mid - 1, key)
        else:
            return search(arr, mid + 1, high, key)
    # right part is sorted
    elif arr[mid] < arr[high]:
        if arr[mid] < key and arr[high] >= key:
            return search(arr, mid + 1, high, key)
        else:
            return search(arr, low, mid - 1, key)
    
    elif arr[low] == arr[mid]:
        if arr[mid] != arr[high]:
            return search(arr, mid + 1, high, key)
        else:
            result = search(arr, low, mid - 1, key)
            if result == -1:
                return search(arr, mid + 1, high, key)
            else:
                return result

# Test cases
a = [15, 16, 19, 20, 25, 1, 5, 6, 6, 6, 10, 14]
x = 5
print search_sorted_rotated(a, x)
