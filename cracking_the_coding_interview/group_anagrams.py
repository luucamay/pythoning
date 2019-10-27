'''
Group Anagrams

Write a method to sort an array ot strings so that all
tne anagrams are next to each other.
Hints:
# 177: think about definition of anagrams
# 182: two anagrams are the same if they have same
chars but in different order.
# 263: can you leverage a standard sorting algorithm?
# 342: do you need to truly sort or just reorganize?
'''
from collections import defaultdict

def group_anagram(strings):
    dictionary = defaultdict(list)
    for x in strings:
        aux = list(x)
        aux.sort()
        key = "".join(aux)
        if not dictionary[key]:
            dictionary[key] = [x]
        else:
            dictionary[key].append(x)
    index = 0
    for key in dictionary:
        arr = dictionary[key]
        for word in arr:
            strings[index] = word
            index += 1
    return strings

# Test
test_list = ['lump', 'eat', 'me', 'tea', 'em', 'plum']
print test_list
print group_anagram(test_list)

