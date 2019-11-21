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
    start = 0
    end = len(arr) - 1
    while start <= end:
        mid = (start + end) // 2
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
            start = mid + 1
        else:
            # check left chunk
            end = mid - 1
    return -1
    

# Test
string = "dad"
arr = ["at", "", "", "", "ball", "", "", "car", "", "", "dad", "", ""]
print sparse_search(string, arr)
