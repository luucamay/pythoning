'''
Petya and Strings - Codeforces
https://codeforces.com/problemset/problem/112/A
'''
words = [None]*2
words[0] = input().lower()
words[1] = input().lower()
new_arr = sorted(words)
if words[0] == words[1]:
    print(0)
elif words[0] == new_arr[0]:
    print(-1)
else:
    print(1)
