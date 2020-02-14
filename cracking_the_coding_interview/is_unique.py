'''
1.1 Is Unique - Cracking the coding interview, P. 101

Implement is_unique function that return True when all the characters in a string are different.
What if you cannot use additional data structures?

Hints
44: Try a hash table
84: There is one solution that is O(N log N) time. Another solution uses some space, but is O(N) time.
132: Can you solve it in O(N log N) time? What might a solution look like?
'''
# First solution
def is_unique1(string):
    n = len (string)
    list_string = sorted(string)
    for i in range (n - 1):
        if list_string[i] == list_string[i +1]:
            return False
    return True
'''
You should check if it is an ascci or unicode
128 characters in ascci alphabet
'''
# Second solution
def is_unique2(string):
    n = len(string)
    letters = [0]*128
    for i in range(n):
        val = ord(string[i])
        if (letters[val]):
            return False
        letters[val] = 1
    return True

# Third solution - using data structure set
def is_unique3(string):
    set_string = set()
    for c in string:
        if c in set_string:
            return False
        else:
            set_string.add(c)
    return True

# Test
print is_unique1("cabdcd")
print is_unique2("cabdcd")
