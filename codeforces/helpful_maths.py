'''
Helpful Maths - Codeforces
'''

given_sum = [int(x) for x in input().split('+')]
given_sum.sort()
given_sum = [str(x) for x in given_sum]
new_sum = '+'
print(new_sum.join(given_sum))
