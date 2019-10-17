'''
Basic Regex Parser
Implement a regular expression function isMatch that supports the '.' and '*' symbols. The function receives two strings - text and pattern - and should return true if the text matches the pattern as a regular expression. For simplicity, assume that the actual symbols '.' and '*' do not appear in the text string and are used as special symbols only in the pattern string.

In case you aren't familiar with regular expressions, the function determines if the text and pattern are the equal, where the '.' is treated as a single a character wildcard (see third example), and '*' is matched for a zero or more sequence of the previous letter (see fourth and fifth examples). 
'''
def is_match(text, pattern):
  return is_match_helper(text, pattern, 0, 0)

def is_match_helper(text, pattern, textIndex, patIndex):
  # print textIndex, patIndex, len(text), len(pattern)
  # base cases
  if textIndex >= len(text):
    if patIndex >= len(pattern):
      return True
    elif patIndex + 1 < len(pattern) and pattern[patIndex + 1] == '*':
      return is_match_helper(text, pattern, textIndex, patIndex + 2)
    else:
      return False
  elif patIndex >= len(pattern) and textIndex < len(text):
    return False
  # check for '*'
  elif patIndex + 1 < len(pattern) and pattern[patIndex + 1] == '*':
    if pattern[patIndex] == '.' or pattern[patIndex] == text[textIndex]:
      return is_match_helper(text, pattern, textIndex, patIndex + 2) or is_match_helper(text, pattern, textIndex + 1, patIndex)
    else:
      is_match_helper(text, pattern, textIndex, patIndex + 2)
  # check for '.' or same char
  elif pattern[patIndex] == '.' or pattern[patIndex] == text[textIndex]:
    return is_match_helper(text,pattern, textIndex + 1, patIndex + 1)
  return False

# Examples:
print is_match('aa','a')
print is_match('aa','aa')
print is_match('abc','a.c')
print is_match('abbb','ab*')

print is_match('a','ab*')
print is_match('ac','ab*')
print is_match('ac','a*c')

# Test
# print is_match('b', '.*.*')
