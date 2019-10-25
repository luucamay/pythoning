'''
A child is running up a staircase with n steps and
can hop either 1 step, 2 steps, or 3 steps at a time.

Implement a method to count how many possible ways
the child can run up the stairs.
'''

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
