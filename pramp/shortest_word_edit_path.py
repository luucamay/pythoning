'''
Shortest Word Edit Path
Given two words source and target, and a list of words words,
find the length of the shortest series of edits
that transforms source to target.

Each edit must change exactly one letter at a time,
and each intermediate word (and the final target word)
must exist in words.

If the task is impossible, return -1.

Examples:
source = "bit", target = "dog"
words = ["but", "put", "big", "pot", "pog", "dog", "lot"]

output: 5
explanation: bit -> but -> put -> pot -> pog -> dog has 5 transitions.

source = "no", target = "go"
words = ["to"]

output: -1
'''

def shortest_word_edit_path(source, target, words):
    queue = [[source, 0]]
    # wordsSet = set(words)
    visited = set()
    while queue:
        source, distance = queue.pop(0)
        visited.add(source)
        if source == target:
            return distance
        for word in words:
            if edited_once(source, word) and word not in visited:
                    queue.append([word, distance + 1])
    return -1

def edited_once(word1, word2):
   s1 = len(word1)
   s2 = len(word2)
   if s1 != s2:
       return False
   diff = 0
   for i in range(s1):
       if word1[i] != word2[i]:
           diff += 1
   if diff == 1:
       return True
   else:
       return False

# Test cases
print shortest_word_edit_path("bit", "dog", ["but","put","big","pot","pog","dog","lot"])
print shortest_word_edit_path("no", "go", ["to"])
print shortest_word_edit_path("bit", "pog", ["but","put","big","pot","pog","pig","dog","lot"])
print shortest_word_edit_path("aa", "bb", ["ab","bb"])
print shortest_word_edit_path("abc", "ab", ["abc","ab"])
print shortest_word_edit_path("aa", "bbb", ["ab","bb"])
