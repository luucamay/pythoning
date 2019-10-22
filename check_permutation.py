'''
Given two string check if one is a permutation of the other.
Hints: White spaces count? case sensitive?
'''
# First solution O(n)
def check_permutation1(a, b):
    size_a = len(a)
    size_b = len(b)
    if size_a != size_b:
        return False

    letters = [0]*128

    for i in range(size_a):
        value = ord(a[i])
        letters[value] += 1
    for j in range(size_b):
        value = ord(b[j])
        letters[value] -= 1
        if letters[value] < 0:
            return False
    return True
# Second solution, sorting O(nlogn)
def check_permutation2(a, b):
    size_a = len(a)
    size_b = len(b)
    if size_a != size_b:
        return False
    a = sorted(a)
    b = sorted(b)
    if a == b:
        return True
    else:
        return False

# Test
print check_permutation1("abcd", "dcba")
print check_permutation2("abcd", "dcba")
