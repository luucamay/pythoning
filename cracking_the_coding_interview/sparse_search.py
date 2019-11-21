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
    print start, end, mid
    if arr[mid] == "":
        left = mid - 1
        right = mid + 1
        while True:
            if left < start and right > end:
                return -1
            elif right <= end and arr[right] != "":
                mid = right
                break
            elif left >= start and arr[left] != "":
                mid = left
                break
            right += 1
            left -= 1
    
    if arr[mid] == string:
        return mid
    elif arr[mid] < string:
        # check right chunk
        return helper(string, arr, mid + 1, end)
    else:
        # check left chunk
        return helper(string, arr, start, mid - 1)
    

# Test
string = "dad"
arr = ["at", "", "", "", "ball", "", "", "car", "", "", "dad", "", ""]
print sparse_search(string, arr)
