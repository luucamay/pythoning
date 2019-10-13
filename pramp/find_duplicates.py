'''
Given two sorted arrays arr1 and arr2 of passport numbers, 
implement a function findDuplicates that returns an array 
of all passport numbers that are both in arr1 and arr2.

Note that the output array should be sorted in an ascending order.
'''
def find_duplicates(arr1, arr2):
  if not arr1 or not arr2:
    return []
  duplicates = []
  i = 0
  j = 0
  while i<len(arr1) and j<len(arr2):
    if arr1[i] == arr2[j]:
      duplicates.append(arr1[i])
      i += 1
      j += 1
    elif arr1[i] > arr2[j]:
      j += 1
    else:
      i += 1
  return duplicates

print find_duplicates([1, 2, 3, 5, 6, 7], [3, 6, 7, 8, 20])