'''
Magic Index
Chapter 8, Problem #3, Cracking the coding interview

A magic index in an array of size n is defined to be an index such that A[i] == i
Given a sorted array of distinct integers, write a method to find a magic index, if one exists, in array A.

Follow up
What if the values are not distinct?

Hints:
#170, #204, #286, #340
'''
def magic_fast(numbers):
    return magic_index(numbers, 0, len(numbers))
def magic_index(numbers, start, end):
    if end < start:
        return -1
    mid = (start + end) // 2
    if mid == numbers[mid]:
        return mid
    # search left
    left_index = min(mid - 1, numbers[mid])
    left = magic_index(numbers, start, left_index)
    if left >= 0:
        return left
    # search right
    right_index = max(mid + 1, numbers[mid])
    right = magic_index(numbers, right_index, end)
    return right

# Test
a = [2, 2, 2]
print magic_fast(a)
