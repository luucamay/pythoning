'''
Young Physicist - CodeForces
https://codeforces.com/problemset/problem/69/A
'''
def is_idle(n, forces):
    x, y, z = 0, 0, 0
    for i in range(n):
        x += forces[i][0]
        y += forces[i][1]
        z += forces[i][2]
    if x != 0 or y != 0 or z != 0:
        return 'NO'
    else:
        return 'YES'

n = int(input())
list_forces = []
for i in range(n):
    force = [int(c) for c in input().split()]
    list_forces.append(force)
print(is_idle(n, list_forces))

