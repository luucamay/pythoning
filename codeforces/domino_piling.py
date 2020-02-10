'''
Domino piling - codeforces
https://codeforces.com/problemset/problem/50/A
'''
def max_num_dominoes(m, n):
    return int(m*n/2)

m, n = [int(x) for x in input().split()]
print(max_num_dominoes(m, n))
