'''
Key Races - Codeforces
https://codeforces.com/problemset/problem/835/A
'''
s, v1, v2, t1, t2 = [int(x) for x in input().split(' ')]
final_time_1 = v1*s + t1*2
final_time_2 = v2*s + t2*2
if final_time_1 < final_time_2:
    print('First')
elif final_time_1 > final_time_2:
    print('Second')
else:
    print('Friendship')

