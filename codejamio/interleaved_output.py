'''
Interleaved output - CodeJamIO
'''
def interleaved_output(string):
    count_i = 0
    count_I = 0
    max_times_ad = 0
    for c in string:
        if c == 'i':
            count_i += 1
        elif c == 'I':
            count_I += 1
        elif c == 'O':
            if count_I > 0:
                count_I -= 1
                max_times_ad += 1
            else:
                count_i -= 1
        else:
            if count_i > 0:
                count_i -= 1
            else:
                count_I -= 1
    return max_times_ad

# Read test
t = int(input())
for i in range(t):
    s = input()
    ans = interleaved_output(s)
    print('Case #{}: {}'.format(i+1, ans))

