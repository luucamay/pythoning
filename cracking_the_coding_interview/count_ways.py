'''
A child is running up a staircase with n steps and
can hop either 1 step, 2 steps, or 3 steps at a time.

Implement a method to count how many possible ways
the child can run up the stairs.
'''

from collections import defaultdict

# A recursive solution found at geeksforgeeks
def findStep( n) :
    if (n == 1 or n == 0) :
        return 1
    elif (n == 2) :
        return 2

    else :
        return findStep(n - 3) + findStep(n - 2) + findStep(n - 1)

# Test code 
n = 4
print(findStep(n))

# A Dinamic Programming solution with memoization found at geekforgeeks
def countWays(n) :
    res = [0] * (n + 1)
    res[0] = 1
    res[1] = 1
    res[2] = 2

    for i in range(3, n + 1) :
        res[i] = res[i - 1] + res[i - 2] + res[i - 3]

    return res[n]

# Test code
n = 4
print(countWays(n))

# Recursive solution from Cracking the coding interview
def count_ways(n):
    if n < 0:
        return 0
    elif n == 0:
        return 1
    else:
        return count_ways(n -1) + count_ways(n-2) + count_ways(n-3)

# Test case
n = 4
print(count_ways(n)) 

# DP with memoization solution from Cracking the coding interview
def find_step_main(n):
    memo = defaultdict(int) # I think we could use a list/array instead
    return find_step(n, memo)
def find_step(n, memo):
    if n < 0:
        return 0
    elif n == 0:
        return 1
    elif memo[n]:
        return memo[n]
    else:
        memo[n] = find_step(n-1, memo) + find_step(n-2, memo) + find_step(n-3, memo)
        return memo[n]

# Test code 
n = 4
print(find_step_main(n))
