'''
The deletion distance of two strings is the minimum number of characters
you need to delete in the two strings in order to get the same string.
For instance, the deletion distance between "heat" and "hit" is 3:

By deleting 'e' and 'a' in "heat", and 'i' in "hit", we get the string "ht" in both cases.
We cannot get the same string from both strings by deleting 2 letters or fewer.
Given the strings str1 and str2, write an efficient function deletionDistance that
returns the deletion distance between them. Explain how your function works,
and analyze its time and space complexities.

Examples:

input:  str1 = "dog", str2 = "frog"
output: 3

input:  str1 = "some", str2 = "some"
output: 0

input:  str1 = "some", str2 = "thing"
output: 9

input:  str1 = "", str2 = ""
output: 0
'''
def deletion_distance(str1, str2):
    s1 = len(str1)
    s2 = len(str2)
    if s1 == 0:
        return s2
    if s2 == 0:
        return s1
    output = 0
    while s1 > 0 and s2 > 0:
        if str1[0] != str2[0]:
            if s1 > s2:
                str1 = str1[1:]
            else:
                str2 = str2[1:]
            output += 1
        else:
            str1 = str1[1:]
            str2 = str2[1:]
        s1 = len(str1)
        s2 = len(str2)
    output += max(s1, s2)
    return output

# Test cases
print deletion_distance("", "")
print deletion_distance("", "hit")
print deletion_distance("neat", "")
print deletion_distance("heat", "hit")
print deletion_distance("hot", "not")
print deletion_distance("some", "thing")
print deletion_distance("abc", "adbc")
print deletion_distance("awesome", "awesome")
print deletion_distance("ab", "ba")
