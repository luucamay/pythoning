'''
Next Round - Codeforces
https://codeforces.com/problemset/problem/158/A
'''
n, k = [int(x) for x in input().split(' ')]
scores = [int(x) for x in input().split(' ')]
counter = 0
for score in scores:
    if score > 0 and score >= scores[k-1]:
        counter += 1
print(counter)
