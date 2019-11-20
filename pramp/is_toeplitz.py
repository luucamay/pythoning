'''
Toeplitz Matrix
A Toeplitz matrix is a matrix where every left-to-right-descending diagonal
has the same element.
Given a non-empty matrix arr, write a function that return
true if and only if it is a Toeplitz matrix.
The matrix can be any dimensions, not necessarily square.

For example,

[[1,2,3,4],
 [5,1,2,3],
 [6,5,1,2]]
is a Toeplitz matrix, so we should return true, while

[[1,2,3,4],
 [5,1,9,3],
 [6,5,1,2]]
isn't a Toeplitz matrix, so we should return false.
'''
def isToeplitz(arr):
  nr = len(arr)
  nc = len(arr[0])
  scol = 0
  srow = nr - 1
  while(srow >= 0 and scol< nc):
    ele = arr[srow][scol]
    r = srow + 1
    c = scol + 1
    while r < nr and c < nc:
      if arr[r][c] != ele:
        return False
      r += 1
      c += 1
    if srow == 0:
      scol += 1
    else:
      srow -= 1
  return True

# Test
matrix = [[1,2,3,4], [5,1,2,3], [6,5,1,2]]
print isToeplitz(matrix)
'''
start at the first column and last row
when reach the first column check the rest of the row

Toeplitz, diagonals from left to right are equal
[[1,2,3,4],
 [5,1,2,3],
 [6,5,1,2]]
nr = 3
nc = 4
check for 1
r = 0, 1, 2
c = 0, 1, 2
check for 2
r = 0, 1, 2
c = 1, 2, 3
check for 3
r = 0, 1
c = 2, 3
check for 4
r = 0
c = 3

'''
