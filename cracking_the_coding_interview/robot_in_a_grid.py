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
