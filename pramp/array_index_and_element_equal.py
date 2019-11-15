'''
Array Index & Element Equality - Pramp

Given a sorted array arr of distinct integers,
write a function indexEqualsValueSearch that
returns the lowest index i for which arr[i] == i.
Return -1 if there is no such index.

Examples:
input: arr = [-8,0,2,5]
output: 2 # since arr[2] == 2
'''
def index_equals_value_search(arr):
  low = 0
  high = len(arr) - 1
  while low <= high:
    mid = (low + high) // 2
    # is the element equal to index?
    if arr[mid] == mid:
      # check if this element is either the first element or 
      # the element before is not equal to its index
      if mid == 0 or arr[mid - 1] < (mid - 1):
        return mid
    if arr[mid] < mid:
      low = mid + 1
    else:
      high = mid - 1    
  return -1

# this approach is not giving me the lowest index OJO
arr = [-2, 1, 2, 3, 4]
print index_equals_value_search(arr)
arr = [-5,0,2,3,10,29,32]
print index_equals_value_search(arr)

'''
find element that is equal to its index
input: arr = [-8,0,1,3,5]
output: 3
low = 0
high = 4
mid = (0 + 4 ) // 2 = 2
arr[mid] = 1
check for low
condition for checking the left: if arr[low] <= low and arr[mid] <= mid

'''