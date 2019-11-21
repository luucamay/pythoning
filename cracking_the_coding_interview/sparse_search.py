'''
Sparse Search - Cracking the coding interview
Chapter 10, Problem #5

Given a sorted array of strings that is interspersed with empety strings,
write a method to find the location of a given string.
Example
Input:
ball, {"at", "", "", "", "ball", "", "", "car", "", "", "dad", "", ""}
Output: 4
Hints: # 256
'''
def sparse_search(string, arr):
    return helper(string, arr, 0, len(arr) - 1)
def helper(string, arr, start, end):
    if end < start:
        return -1
    mid = (start + end) // 2
    if arr[mid] == string:
        return mid
    if arr[mid] != "":
        if arr[mid] < string:
            # check right chunk
            helper(string, arr, mid + 1, end)
        else:
            # check left chunk
            helper(string, arr, start, mid - 1)
    left = helper(string, arr, start, mid - 1)
    if left >= 0:
        return left
    right = helper(string, arr, mid + 1, end)
    return right

# Test
string = "dad"
arr = ["at", "", "", "", "ball", "", "", "car", "", "", "dad", "", ""]
print sparse_search(string, arr)
