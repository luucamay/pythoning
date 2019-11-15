'''
Revesrse Polish Notation Calculator - Daily Interview Problem

Given an expression (as a list) in reverse polish notation, evaluate the expression.
Reverse polish notation is where the numbers come before the operand.
Note that there can be the 4 operands '+', '-', '*', '/'.
You can also assume the expression will be well formed.

Example
Input: [1, 2, 3, '+', 2, '*', '-']
Output: -9
The equivalent expression of the above reverse polish notation would be (1 - ((2 + 3) * 2)).
'''
def reverse_polish_notation(expr):
    stack = []
    for x in expr:
        try:
            num = int(x)
            stack.append(num)
        except:
            right, left = stack.pop(), stack.pop()
            if x == '+':
                stack.append(left + right)
            elif x == '-':
                stack.append(left - right)
            elif x == '*':
                stack.append(left * right)
            else:
                stack.append(int(float(left) / right))
    
    return stack.pop()

# Test
print(reverse_polish_notation([1, 2, 3, '+', 2, '*', '-']))

