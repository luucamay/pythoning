"""
Stones on the Table - Codeforces
https://codeforces.com/problemset/problem/266/A
"""
def min_number_stones(rsize, stones):
    taken_stones = 0
    for i in range(rsize-1):
        if stones[i] == stones[i+1]:
            taken_stones += 1
    return taken_stones

n = int(input())
s = input()
print(min_number_stones(n, s))
