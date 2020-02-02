'''
A. Theatre Square
https://codeforces.com/problemset/problem/1/A
'''
import math
new_input = input().split(' ')
n, m, a = [int(x) for x in new_input]
result = math.ceil(n/a)*math.ceil(m/a)
print(result)
