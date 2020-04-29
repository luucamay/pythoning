'''
Chat room - Codeforces
https://codeforces.com/problemset/problem/58/A

Problem Details:
    word_base = "hello"

    example:
        input: hlelo
        la primera letra de input es h?
            si
                la siguiente letra es e?
                    si
                    no
                        la siguienta letra es h?
                        si
                            busca e

# rules:
    - if count size of input string is less than 5 print NO
    - if we found the "hello" stop traversing the input and print YES
    - if curr_char_input is equal to char_to_find
        - yes, update char_to_find to next_char_from_word_base, check next_char_input
        - no
            - check curr_char_input is repeated, or first char (same as last one)
            - check next_char_input<<<----

test:
input = 'hlelo'
             ^
curr_char_input = o
char_to_find = l <---- no more chars to find, return YES, break
j = 3
'''
def word_typed (string):
    word_base = 'hello'
    j = 0
    n = len(string)
    char_to_find = word_base[j]
    for i in range(n):
        curr_char_input = string[i]
        if curr_char_input == char_to_find:
            j += 1
            if j == 5:
                return 'YES'
            char_to_find = word_base[j]
    return 'NO'

s = input()
print(word_typed(s))

