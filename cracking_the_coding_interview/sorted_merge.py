'''
Sorted Merge
You are given two arrays A and B that are sorted. Write a function to merge B into A.
Consider that A has enough space to allocate all of the values of B.

Hints
# 332: Try moving from the end of array to the beginning
'''
# Solution 1: using extra memory
def merge1(a, b):
    sizeB = len(b)
    sizeA = len(a)
    new_array = []
    i = 0
    j = 0
    while j < len(b) and i < sizeA:
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

# Test
A = [10, 20, 25, 30, 31]
B = [5, 15, 16, 17, 40, 42]
print merge1(A,B)

# Solution 2: thanks to hint, start array a from back
# This solution doesn't work because it is never assigning value at the end of the list
def merge2(a, b):
    sizeB = len(b)
    sizeA = len(a) - sizeB
    for j in range(sizeB):
        i = sizeA - 1 # start at last element
        while i >= 0 and b[j] < a[i]:
            a[i], a[i + 1] = b[j], a[i] # swap
            i -= 1
    return a

# Test
# print merge2(A,B)

# Solution 3: translated code from Java in the book of cracking the coding interview to Python
# start both indexes at the end
def merge3(a, b):
    indexA = len(a) - 1
    indexB = len(b) - 1
    aux = [None]*len(b)
    a.extend(aux)
    indexMerge = indexA + indexB + 1
    while indexB >= 0:
        if indexA >= 0 and a[indexA] > b[indexB]:
            a[indexMerge] = a[indexA]
            indexA -= 1
        else:
            a[indexMerge] = b[indexB]
            indexB -= 1
        indexMerge -= 1
# Test
print merge3(A,B)
print A