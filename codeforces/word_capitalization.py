"""
Codeforces - Word Capitalization
https://codeforces.com/problemset/problem/281/A

Capitalizate the first letter in a word.
"""
def capitalizate(string):
    answer = string[0].upper() + string[1:]
    return answer

word = input()
print(capitalizate(word))
