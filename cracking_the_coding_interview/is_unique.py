'''
Implement is_unique function that return True when all the characters in a string are different.
'''
# First solution
def is_unique1(string):
    n = len (string)
    new_string = sorted(string)
    for i in range (n - 1):
        if new_string[i] == new_string[i +1]:
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

# Test
print is_unique1("cabdcd")
print is_unique2("cabdcd")
