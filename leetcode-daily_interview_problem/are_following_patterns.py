'''
Are following patterns - Code Signal

Given an array strings, determine whether it follows the sequence given in the patterns array.
In other words, there should be no i and j for which strings[i] = strings[j] and patterns[i] != patterns[j]
or for which strings[i] != strings[j] and patterns[i] = patterns[j].

Example

For strings = ["cat", "dog", "dog"] and patterns = ["a", "b", "b"], the output should be
areFollowingPatterns(strings, patterns) = true;
For strings = ["cat", "dog", "doggy"] and patterns = ["a", "b", "b"], the output should be
areFollowingPatterns(strings, patterns) = false.
'''

def areFollowingPatterns(strings, patterns):
    d = {}
    for i, j in zip(strings, patterns):
        if i in d and d[i] != j:
            return False
        d[i] = j
    return len(d) == len(set(d.values()))
# Test
strings = ['dos', 'tres', 'tres']
patterns = ['a', 'b', 'b']
print areFollowingPatterns(strings, patterns)
