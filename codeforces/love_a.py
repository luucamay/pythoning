'''
Love "A" - Codeforces
https://codeforces.com/problemset/problem/1146/A
'''
import math

s = input()
size = 0
count_a = 0
# n = len(s)
for c in s:
    size += 1
    if c == 'a':
        count_a += 1
diff = size - count_a
half = math.ceil(size/2)
if diff < half:
    print(size)
else:
    print('diff', diff, 'half', half, 'as', count_a)
    print(diff - count_a)

