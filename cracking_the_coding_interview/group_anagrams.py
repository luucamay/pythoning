'''
Group Anagrams

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

