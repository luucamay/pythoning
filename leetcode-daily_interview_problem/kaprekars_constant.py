'''
Kaprekars constant - Daily interview problem

Kaprekars constant is the number 6174.
This number is special because it has the property where for any 4-digit number
that has 2 or more unique digits, if you repeatedly apply a certain function
it always reaches the number 6174.

This certain function is as follows:
- Order the number in ascending form and descending form to create 2 numbers.
- Pad the descending number with zeros until it is 4 digits in length.
- Subtract the ascending number from the descending number.
- Repeat.

Given a number n, find the number of times the function needs to be applied
to reach Kaprekar's constant.
'''
def two_different_digits(number):
    if number <= 10 or number > 9999:
        return False
    my_set = set()
    while number > 0 :
        current = number % 10
        number = number // 10
        my_set.add(current)
    if len(my_set) >= 2:
        return True
    return False

def num_kaprekar_iterations(number):
    KAPREKAR_CONSTANT = 6174
    if not two_different_digits(number):
        return -1
    counter = 0
    while number != KAPREKAR_CONSTANT:
        number = get_kaprekar_constant(number)
        counter += 1
    return counter

def get_kaprekar_constant(number):
    digits = [0]*4
    for i in range(4):
        if number > 0:
            dig = number % 10
            digits[i] = dig
            number = number // 10
    digits.sort()
    asc = 0
    for i in range(4):
        asc = asc*10 + digits[i]

    digits.sort(reverse = True)
    desc = 0
    for i in range(4):
        desc = desc*10 + digits[i]
    return abs(asc - desc)

# Test cases
print num_kaprekar_iterations(123)
print num_kaprekar_iterations(1000)
print num_kaprekar_iterations(1112)
print num_kaprekar_iterations(9812)
