'''
Football - Codeforces
https://codeforces.com/problemset/problem/96/A
'''
situation = input()
ceros = '0000000'
ones = '1111111'
if ceros in situation or ones in situation:
    print('YES')
else:
    print('NO')
