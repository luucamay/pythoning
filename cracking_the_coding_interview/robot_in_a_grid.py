'''
Robot in a Grid
Cracking the coding interview, chapter 8, exercise #2

Imagine a robot sitting on the upper left corner of grid with r rows and c columns.
The robot can only move in two directions, right and down, but certain cells are "off limits" such that
the robot cannot step on them. Design an algorithm to find a path for the robot from the top left to
the bottom right.
Hints:
#331: For the robot to reach the last cell, it must find a path to the second-to-last cells. For it to
find a path to the second-to-last cells, it must find a path to the third-to-last cells.
#360: Simplify this problem a bit by first figuring out if there's a path. Then, modify your algorithm to track the path.
#388: Think again about the efficiency of your algorithm. Can you optimize it?
'''
def get_path(grid):
    if grid == None or len(grid) == 0:
        return []
    points = []
    failed_points = set()
    path(grid, len(grid) - 1, len(grid[0]) - 1, points, failed_points)
    return points

def path(grid, row, col, points, failed_points):
    if row < 0 or col < 0 or not grid[row][col]:
        return False
    point = (row, col)
    if point in failed_points:
        return False
    # is at origin
    if row == 0 and col == 0:
        points.append(point)
        return True
    if path(grid, row - 1, col, points, failed_points) or path(grid, row, col - 1, points, failed_points):
        points.append(point)
        return True
    failed_points.add(point)
    return False

# Test
grid = [[1, 1, 1, 0], [1, 0, 1, 1], [0, 1, 1, 1]]
print get_path(grid)
