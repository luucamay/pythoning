'''
Team - CodeForces

This contest offers n problems to the participants. For each problem we know, which friend is sure about the solution. Help the friends find the number of problems for which they will write a solution.

More details of the problem: 
    https://codeforces.com/problemset/problem/231/A
'''
def to_be_implemented(a, b, c,):
    ones = 0
    if a == 1:
        ones += 1
    if b == 1:
        ones += 1
    if c == 1:
        ones += 1
    if ones > 1:
        return 1
    return 0

n = int(input())
num_to_implement = 0
for i in range(n):
    a, b, c = [int(x) for x in input().split()]
    num_to_implement += to_be_implemented(a,b,c)

print(num_to_implement)


