'''
Word Count Engine - Pramp

Implement a document scanning function wordCountEngine, which receives a string
document and returns a list of all unique words in it and their number of
occurrences, sorted by the number of occurrences in a descending order.
If two or more words have the same count, they should be sorted according to their
order in the original sentence. Assume that all letters are in english alphabet.
You function should be case-insensitive, so for instance, the words "Perfect" and
"perfect" should be considered the same word.

The engine should strip out punctuation (even in the middle of a word) and use
whitespaces to separate words.

Analyze the time and space complexities of your solution. Try to optimize for
time while keeping a polynomial space complexity.

Examples:
input:  document = "Practice makes perfect. you'll only
                    get Perfect by practice. just practice!"
output: [ ["practice", "3"], ["perfect", "2"],
          ["makes", "1"], ["youll", "1"], ["only", "1"], 
          ["get", "1"], ["by", "1"], ["just", "1"] ]
'''
from collections import OrderedDict
def word_count_engine(document):
  document = document.lower()
  words = document.split(' ')
  # clean words 97 => a, 122 => z
  d = OrderedDict()
  for w in words:
    w = clean_word(w)
    if w == '':
      continue
    if w in d:
      d[w] += 1
    else:
      d[w] = 1
    
  output = []
  for k in d:
    output.append([k, str(d[k])])
  # sort
  output.sort(key= lambda x:x[1],reverse=True)
  return output

def clean_word(word):
  out = ''
  for c in word:
    if c >= 'a' and c <= 'z':
      out += c
  return out

document = "Every book is a quotation; and every house is a quotation out of all forests, and mines, and stone quarries; and every man is a quotation from all his ancestors. "
print word_count_engine(document)

'''
input:  document = "Practice makes perfect. you'll only
                    get Perfect by practice. just practice!"

output: [ ["practice", "3"], ["perfect", "2"],
          ["makes", "1"], ["youll", "1"], ["only", "1"], 
          ["get", "1"], ["by", "1"], ["just", "1"] ]
not solved:
if two words same count then sorted as in the original array
clean the input to remove not desired symbols

strip the input => get word elements
clean the input to remove not desired symbols
count words in the hashmap
key is a word, value is occurrences, use lambda'''

