'''
Pairs with Specific Difference

Given an array arr of distinct integers and a nonnegative integer k,
write a function findPairsWithGivenDifference that returns an array of
all pairs [x, y] in arr, such that x - y = k. If no such pairs exist,
return an empty array.

Note: the order of the pairs in the output array should maintain the order
of the y element in the original array.
'''
# My solution
def find_pairs_with_given_difference(arr, k):
    my_set = set(arr)
    pairs = []
    for y in arr:
        x = k + y
        if x in my_set and x != y:
            pairs.append([x, y])
    return pairs
# Test cases
arr = [4,1]
k = 3
print find_pairs_with_given_difference(arr, k)
print find_pairs_with_given_difference([1,5,11,7], 4)
print find_pairs_with_given_difference([1,5,11,7], 6)
print find_pairs_with_given_difference([1,5,11,7], 10)
print find_pairs_with_given_difference([0,-1,-2,2,1], 1)
print find_pairs_with_given_difference([1,7,5,3,32,17,12], 17)
