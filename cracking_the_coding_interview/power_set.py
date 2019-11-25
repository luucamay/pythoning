'''
Power Set - Cracking the coding interview
Chapter 8, Problem #3
Write a method to return all subsets of a set.

Hints:
#273, #290, #338, #354, #373
'''
def get_subsets(iset):
    if not iset:
        return [set()]
    item = iset.pop()
    subsets = get_subsets(iset)
    more_subsets = []
    for s in subsets:
        new_s = set()
        new_s.update(s)
        new_s.add(item)
        more_subsets.append(new_s)
    subsets.extend(more_subsets)
    return subsets

# Print
# my_set = set(['a', 'b'])
my_set = set(['a', 'b', 'c', 'd'])
print get_subsets(my_set)

