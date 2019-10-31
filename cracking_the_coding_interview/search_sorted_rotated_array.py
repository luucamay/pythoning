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
    else:
        if arr[mid] < key and arr[high] >= key:
            return search(arr, mid + 1, high, key)
        else:
            return search(arr, low, mid - 1, key)

# Test cases
a = [15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14]
x = 5
print search_sorted_rotated(a, x)
