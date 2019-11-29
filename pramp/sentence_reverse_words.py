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
  word = []
  spaces = []
  output = []
  for c in arr:
    if c == ' ':
      spaces.append(c)
      if word:
        output = word + output
      word = []
    else:
      word.append(c)
      if spaces:
        output = spaces + output
      spaces = []
  output = spaces + word + output
  return output

# Test
arr = [ 'p', 'e', 'r', 'f', 'e', 'c', 't', ' ', 'm', 'a', 'k', 'e', 's', ' ', ' ', 'p', 'r', 'a', 'c', 't', 'i', 'c', 'e' ]
print reverse_words(arr)

# Second approach
def mirror_reverse(arr, start, end):
  while start < end:
    arr[start], arr[end] = arr[end], arr[start]
    start += 1
    end -= 1
def reverse_words_elegant(arr):
    n = len(arr)
    mirror_reverse(arr, 0, n-1)
    word_start = -1
    for i in range(n):
      if arr[i] == ' ':
        if word_start >= 0:
          mirror_reverse(arr, word_start, i-1)
          word_start = -1
      elif i == (n-1):
        if word_start >= 0:
          mirror_reverse(arr, word_start, i)
      elif word_start == -1:
        word_start = i
    return arr

# Test
arr = [ 'p', 'e', 'r', 'f', 'e', 'c', 't', ' ', 'm', 'a', 'k', 'e', 's', ' ', ' ', 'p', 'r', 'a', 'c', 't', 'i', 'c', 'e' ]
print reverse_words_elegant(arr)
            
            