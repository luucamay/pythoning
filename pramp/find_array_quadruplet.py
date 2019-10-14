'''
Given an unsorted array of integers arr and a number s, write a function findArrayQuadruplet
that finds four numbers (quadruplet) in arr that sum up to s.
Your function should return an array of these numbers in an ascending order.
If such a quadruplet doesn’t exist, return an empty array.

Note that there may be more than one quadruplet in arr whose sum is s.
You’re asked to return the first one you encounter (considering the results are sorted).
'''
def find_array_quadruplet(arr, s):
  n = len(arr)
  if n < 4:
    return []
  arr.sort()
  for i in range(n - 3):
    for j in range(i + 1, n - 2):      
      low = j + 1
      high = n - 1
      r = s - (arr[i] + arr[j])
      while low < high:
        aux = arr[low] + arr[high]
        if r > aux:
          low +=1
        elif r < aux:
          high -=1
        else:
          return [arr[i], arr[j], arr[low], arr[high]]
  return []

# myarray = [2, 7, 4, 0, 9, 5, 1, 3]
myarray = [4,4,4,4]
s = 16
print find_array_quadruplet(myarray, s)
