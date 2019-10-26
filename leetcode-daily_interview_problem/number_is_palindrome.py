'''
Palindrome Integers
Given an integer, check if that integer is a palindrome. For this problem do not convert the integer to a string to check if it is a palindrome.
'''
# Solution building reversing number
def is_palindrome(n):
    number = n
    new_number = 0
    while number > 0:
        remainder = number % 10
        new_number = new_number*10 + remainder
        number = number // 10
    return new_number == n

# Solution building only the half of the number
def isPalindrome(x):
    """
    :type x: int
    :rtype: bool
    """
    if x < 0 or (x % 10 == 0 and x != 0):
        return False
    
    new_number = 0
    while x > new_number:
        new_number = new_number*10 + x % 10
        x = x // 10
    return x == new_number or x == new_number//10

# Test cases
print is_palindrome(1234321)
print is_palindrome(1234322)

print isPalindrome(1234321)
print isPalindrome(1234322)