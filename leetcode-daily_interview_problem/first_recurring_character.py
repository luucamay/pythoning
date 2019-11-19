'''
First recurring character - Daily Interview Problem
'''
def first_recurring_char(s):
    d = {}
    for c in s:
        if c in d:
            return c
        else:
            d[c] = 1
    return None

# Test
print first_recurring_char('qwerttyy')
print first_recurring_char('qwerty')
