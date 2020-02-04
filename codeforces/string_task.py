'''
String Task - Codeforces
https://codeforces.com/problemset/problem/118/A
'''
string = input()
string = string.lower()
vowels = set(['a', 'e', 'i', 'o', 'u', 'y'])
answer = ''
for char in string:
    if char not in vowels:
        answer = answer + '.' + char
print(answer)
