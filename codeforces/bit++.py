'''
Bit++ 
Problem description: https://codeforces.com/problemset/problem/282/A
'''
def exec_statement(x, string):
    if string.find('+') >= 0:
        x += 1
    elif string.find('-') >= 0:
        x -= 1
    return x

x = 0
n = int(input())
for _ in range(n):
    statement = input()
    x = exec_statement(x, statement)
print(x)
