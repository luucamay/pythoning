'''
A. Theatre Square
https://codeforces.com/problemset/problem/1/A
'''

import math

n, m, a = [int(x) for x in input().split(' ')]
ans = math.ceil(n/a) * math.ceil(m/a)
print(ans)
