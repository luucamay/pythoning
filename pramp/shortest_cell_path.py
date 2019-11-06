'''
Shortest cell path - Pramp

In a given grid of 0s and 1s, we have some starting row and column sr, sc and
a target row and column tr, tc. Return the length of the shortest path
from sr, sc to tr, tc that walks along 1 values only.

Each location in the path, including the start and the end, must be a 1.
Each subsequent location in the path must be 4-directionally adjacent to the previous location.

It is guaranteed that grid[sr][sc] = grid[tr][tc] = 1,
and the starting and target positions are different.

If the task is impossible, return -1.

Examples:

input:
grid = [[1, 1, 1, 1], [0, 0, 0, 1], [1, 1, 1, 1]]
sr = 0, sc = 0, tr = 2, tc = 0
output: 8
(The lines below represent this grid:)
1111
0001
1111

grid = [[1, 1, 1, 1], [0, 0, 0, 1], [1, 0, 1, 1]]
sr = 0, sc = 0, tr = 2, tc = 0
output: -1
(The lines below represent this grid:)
1111
0001
1011
'''
def shortestCellPath(grid, sr, sc, tr, tc):
  num_row = len(grid)
  num_col = len(grid[0])
  visited = set()
  current = [(sr, sc, 0)]
  while current: 
    r, c, d = current.pop(0)
    if r == tr and c == tc:
      return d
    visited.add((r, c))
    for nr, nc in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)):
        if nr >= 0 and nr < num_row and nc >= 0 and nc < num_col: # not out of the grid
            if grid[nr][nc] == 1 and (nr, nc) not in visited:
                current.append((nr, nc, d + 1))
  return -1

# Test cases:
grid = [[1, 1, 1, 1], [0, 0, 0, 1], [1, 0, 1, 1]]
sr = 0
sc = 0
tr = 2
tc = 0
print shortestCellPath(grid, sr, sc, tr, tc)

grid = [[1, 1, 1, 1], [0, 0, 0, 1], [1, 1, 1, 1]]
sr = 0
sc = 0
tr = 2
tc = 0
print shortestCellPath(grid, sr, sc, tr, tc)
