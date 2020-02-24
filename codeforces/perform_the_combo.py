'''
Perform the combo - Codeforces
https://codeforces.com/contest/1311/problem/C
'''
# Solution #1: Time limit exceed!
def times_button_pressed(n, m, combo, mistakes):
    nro_times = [0]*26
    for c in combo:
        pos = ord(c) - 97
        nro_times[pos] += 1
    # m wrong attempts
    for i in range(m):
        p = mistakes[i]
        for j in range(p):
            button = combo[j]
            pos = ord(button) - 97
            nro_times[pos] += 1
    return nro_times

# Solution #2
def times_button_pressed2(n, m, combo, mistakes):
    times_pressed = {}
    for c in combo:
        if c in times_pressed:
            times_pressed[c] += 1
        else:
            times_pressed[c] = 1
    for i in range(m):
        p = mistakes[i]
        for j in range(p):
            button = combo[j]
            times_pressed[button] += 1
    nro_times = [0]*26
    for c in times_pressed:
        nro_times[ord(c) - 97] = times_pressed[c]
    return nro_times

# Solution #3
def times_button_pressed3(n, m, combo, mistakes):
    times_pressed = [0]*26
    for i in range(n):
        c = combo[i]
        pos = ord(c) - 97
        times_pressed[pos] += 1
        times_c = 0
        for j in range(m):
            p = mistakes[j]
            if i < p:
                times_c += 1
        times_pressed[pos] += times_c
    return times_pressed

t = int(input())
for _ in range(t):
    n, m = [int(x) for x in input().split()]
    combo = input()
    mistakes = [int(x) for x in input().split()]
    # ouput is an array of numbers
    output = times_button_pressed3(n, m, combo, mistakes)
    string_output = ''
    for i in range(25):
        string_output = string_output + str(output[i]) + ' '
    string_output += str(output[25])
    print(string_output)
    
