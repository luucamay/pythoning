'''
Sorted Merge
You are given two arrays A and B that are sorted. Write a function to merge B into A.
Consider that A has enough space to allocate all of the values of B.

Hints
# 332: Try moving from the end of array to the beginning
'''
# Solution 1: using extra memory
def merge1(a, b):
    new_array = []
    i = 0
    j = 0
    while j < len(b) and i < len(a):
        if a[i] > b[j]:
            new_array.append(b[j])
            j += 1
        else:
            new_array.append(a[i])
            i += 1
    if i < len(a):
        new_array.extend(a[i:])
    else:
        new_array.extend(b[j:])
    return new_array
A = [10, 20, 25, 30, 32, 50]
B = [5, 15, 16, 17, 40, 42]
print merge1(A,B)