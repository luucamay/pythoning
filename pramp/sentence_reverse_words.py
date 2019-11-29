'''
Sentence Reverse - Pramp

You are given an array of characters arr that consists of sequences of characters separated by
space characters. Each space-delimited sequence of characters defines a word.
Implement a function reverseWords that reverses the order of the words in the array
in the most efficient manner.
Explain your solution and analyze its time and space complexities.

Example:
input:  arr = [ 'p', 'e', 'r', 'f', 'e', 'c', 't', '  ',
                'm', 'a', 'k', 'e', 's', '  ',
                'p', 'r', 'a', 'c', 't', 'i', 'c', 'e' ]
output: [ 'p', 'r', 'a', 'c', 't', 'i', 'c', 'e', '  ',
          'm', 'a', 'k', 'e', 's', '  ',
          'p', 'e', 'r', 'f', 'e', 'c', 't' ]
'''
def reverse_words(arr):
  n = len(arr)
  word = []
  spaces = []
  output = []
  for i in range(n):
    if arr[i] == ' ':
      spaces.append(arr[i])
      if i == (n - 1) or arr[i + 1] != ' ' :
        output = word + output
        output = spaces + output
        word = []
        spaces = []
    else:
      word.append(arr[i])
      if i == (n - 1):
        output = word + output
  return output