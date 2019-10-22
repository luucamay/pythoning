'''
Given two string check if one is a permutation of the other.
Hints: White spaces count? case sensitive?
'''
def check_permutation(a, b):
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

# Test
print check_permutation("abcdd", "adcba")
