'''
Merging 2 Packages - Pramp

Given a package with a weight limit limit and an array arr of item weights,
implement a function getIndicesOfItemWeights that finds two items whose sum
of weights equals the weight limit limit. Your function should return a pair [i, j]
of the indices of the item weights, ordered such that i > j.
If such a pair doesn’t exist, return an empty array.

Analyze the time and space complexities of your solution.

Example:
input:  arr = [4, 6, 10, 15, 16],  lim = 21
output: [3, 1]
'''
def get_indices_of_item_wights(arr, limit):
  num_map = {}
  n = len(arr)
  
  output = []
  
  for i in range(n):
    x = limit - arr[i]
    if x in num_map:
      j = num_map[x]
      output = [i, j]
    
    num_map[arr[i]] = i
      
  return output

# Test
arr = [4,4,4]
limit = 8
print get_indices_of_item_wights(arr, limit)

# Approach on October 29th
from collections import defaultdict
def get_indices_of_item_wights(arr, limit):
  my_dict = defaultdict(list)
  output = []
  for j in range(len(arr)):
    if my_dict[arr[j]]:
      my_dict[arr[j]].append(j)
    else:
      my_dict[arr[j]] = [j]
    
  for i in range(len(arr)):
    x = limit - arr[i]
    if x in my_dict:
      for index in my_dict[x]:
        if i > index:
          output = [i, index] 
          

  return output

# Test
arr = [4, 6, 10, 15, 16]
lim = 21
print get_indices_of_item_wights(arr, lim)