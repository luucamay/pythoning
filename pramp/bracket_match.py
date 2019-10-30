'''
Bracket Match

A string of brackets is considered correctly matched if every opening bracket in the string
can be paired up with a later closing bracket, and vice versa.
For instance, '(())()' is correctly matched, whereas ')(' and '((' aren't.
For instance, '((' could become correctly matched by adding two closing brackets at the end,
so you'd return 2.

Given a string that consists of brackets, write a function bracketMatch
that takes a bracket string as an input and returns the minimum number of brackets
you'd need to add to the input in order to make it correctly matched.

Explain the correctness of your code, and analyze its time and space complexities.

Examples:

input:  text = '(()'
output: 1

input:  text = '(())'
output: 0

input:  text = '())('
output: 2
'''
def bracket_match(text):
  size = len(text)
  if size == 0:
    return 0
  opens = 0
  closes = 0
  output = 0
  for c in text:
    if c == '(':
      opens += 1
    else:
      closes += 1
    if closes > opens:
      output += 1
      opens += 1
  output = output + (opens - closes)
  return output

# Test
text = "())("
print bracket_match(text)