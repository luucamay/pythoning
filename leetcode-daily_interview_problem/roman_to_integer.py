'''
Roman to Integer
Leetcode #13
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, two is written as II in Roman numeral, just two one's added together. Twelve is written as, XII, which is simply X + II. The number twenty seven is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9.
X can be placed before L (50) and C (100) to make 40 and 90.
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer. Input is guaranteed to be within the range from 1 to 3999.
'''

'''
notes:
    *largest to smallest from left to right (sum)
special cases:
    - I, check if next is V or X
    - X, check if next is L or C
    - C, check if next is D or M

d['I']=1
V-> 5
X-> 10
L-> 50
C-> 100
D-> 500
M-> 1000

input-> XCIII

1. traverse the input string
2. add their value to total
*check if there is a different symbol that is not in the dictionary
if only one element return its value
* if current is I and next is (V or X) --> substrat with next and add that value to total and jump one position
* the same for X and C
'''
def romanToInt(string):
    d={
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000
        }
    n = len(string)
    i = 0
    total = 0
    while i < n:
        curr_char = string[i]
        if i < n-1: 
            next_char = string[i+1]
            special_i = curr_char == 'I' and next_char in ['V', 'X']
            special_x = curr_char == 'X' and next_char in ['L', 'C']
            special_c = curr_char == 'C' and next_char in ['D', 'M']
            if special_i or special_x or special_c:
                diff = d[next_char]-d[curr_char]
                total += diff
                i += 1
            elif d[curr_char] >= d[next_char]:
                total += d[curr_char]
            else:
                return total
        else:
            total += d[curr_char]
        i += 1
    return total

roman_str = input()
print(romanToInt(roman_str))
       

