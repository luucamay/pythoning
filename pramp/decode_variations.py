'''
Decode Variations - Pramp

A letter can be encoded to a number in the following way:

'A' -> '1', 'B' -> '2', 'C' -> '3', ..., 'Z' -> '26'
A message is a string of uppercase letters, and it is encoded first using this scheme. For example, 'AZB' -> '1262'

Given a string of digits S from 0-9 representing an encoded message, return the number of ways to decode it.

Examples:

input:  S = '1262'
output: 3
explanation: There are 3 messages that encode to '1262': 'AZB', 'ABFB', and 'LFB'.
'''
# My approach, time complexity is exponential
def decodeVariations(S):
  def decodable(value):
    size = len(value)
    if size == 1:
      if int(value) == 0:
        return False
      else:
        return True
    elif size == 2:
      if int(value) >= 10 and int(value) <= 26:
        return True
      else:
        return False
    return False
  
  n = len(S)
  if n == 0:
    return 1
  elif n == 1:
    if decodable_as_single_number(S):
      return 1
    else:
      return 0
  else:
    return decodeVariations(S[:n-1]) * int(decodable(S[n-1])) + decodeVariations(S[:n-2]) * int(decodable(S[n-2:]))