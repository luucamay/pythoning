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

# Test
print is_unique1("cabdcd")
