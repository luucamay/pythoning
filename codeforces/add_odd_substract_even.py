'''
Add Odd or Subsctract Even - Codeforces
https://codeforces.com/contest/1311/problem/A
'''
def modify(a, b):
    count = 0
    if a == b:
        return count
    count += 1
    diff = a - b
    # b is bigger
    if diff < 0:
        if diff%2 == 0:
            return count + 1
        else:
            return count
    else:
        if diff%2 == 0:
            return count
        else:
            return count + 1

t = int(input())
for case in range(t):
    a, b = [int(x) for x in input().split()]
    modifications = modify(a,b)
    print(modifications)

