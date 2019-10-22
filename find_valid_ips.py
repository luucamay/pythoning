'''
Restore IP Addresses

Given a string containing only digits, retrun the possible IP addresses
you can make with that string by spliting into 4 parts of A, B, C, D.

An IP Address is in the format of A.B.C.D,
where A,B,C,D are all integeres between 0 to 255.
Keep in mind that integers can't start with a 0! (Except for 0)
'''
# Iterative solution
def find_valid_ips(numbers):
    ips = []
    n = len(numbers)
    if n > 3 and n < 13:
        for i in range(1,4):
            a = numbers[:i]
            if is_valid(a) and (n - i) > 1:
                for j in range(i + 1, i + 4):
                    b = numbers[i:j]
                    if is_valid(b) and (n - j) > 1:
                        for k in range(j + 1, j + 4):
                            c = numbers[j:k]
                            d = numbers[k:]
                            if is_valid(c) and is_valid(d):
                                ips.append(a + '.' + b + '.' + c + '.' + d)
    return ips

def is_valid(string):
    n = len(string)
    if n < 1 or n > 3:
        return False
    if n > 1 and string[0] == '0':
        return False
    if int(string) > 255 or int(string) < 0:
        return False
    return True

# Test
t1 = '12345'
t2 = '1592551013'
t3 = '00100'
print find_valid_ips(t3)
