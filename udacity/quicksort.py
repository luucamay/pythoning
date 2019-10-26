def quicksort(array):
    return quicksort_helper(array, 0, len(array) - 1)

def quicksort_helper(elements, start, end):
    if start < end:
        pivot_index = partition(elements, start, end)
        quicksort_helper(elements, start, pivot_index - 1)
        quicksort_helper(elements, pivot_index + 1, end)
    return elements

def partition(elements, start, end):
    storeIndex = start + 1
    for i in range(start + 1, end + 1):
        if elements[i] < elements [start]:
            elements[storeIndex], elements[i] = elements[i], elements[storeIndex]
            storeIndex += 1
    elements[start], elements[storeIndex - 1] = elements[storeIndex - 1], elements[start]

    return storeIndex - 1

# Test
# test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
test = [3, 44, 38, 5, 47, 15, 36, 26, 27, 2, 46, 4, 19, 50, 48]
print test
print quicksort(test)
