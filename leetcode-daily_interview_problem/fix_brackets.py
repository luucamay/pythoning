'''
Fix brackets - Minimum add to make parentheses valid

Given a string S of '(' and ')' parentheses, we add the minimum number of parentheses ( '(' or ')', and in any positions ) so that the resulting parentheses string is valid.

Formally, a parentheses string is valid if and only if:

It is the empty string, or
It can be written as AB (A concatenated with B), where A and B are valid strings, or
It can be written as (A), where A is a valid string.
Given a parentheses string, return the minimum number of parentheses we must add to make the resulting string valid.

'''
def min_add_to_make_valid(s):
    min = 0
    counter = 0
    for i in range(len(s)):
        if s[i] == '(':
            counter += 1
        else:
            counter -= 1
        if counter < 0:
            counter += 1
            min += 1
    return min + counter

# Test cases
print min_add_to_make_valid('(()()') # 1
print min_add_to_make_valid('())') # 1
print min_add_to_make_valid('(((') # 3
print min_add_to_make_valid('()') # 0
print min_add_to_make_valid('()))((') # 4