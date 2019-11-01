'''
Is Shiftet - Daily Interview Problem
Given two strings find out if they are the same but in rotated order
'''
def is_shifted(A, B):
    '''
    if len(A) == len(B) and len(A) > 0:
        indexB = B.find(A[0])
        if indexB:
            for indexA in range(len(A)):
                if A[indexA] == B[indexB]:
                        indexB += 1
                        indexB = indexB % len(B)
                else:
                    return False
            return True
    return False
    '''
    size1 = len(A)
    size2 = len(B)
    temp = ''
    if size1 != size2:
        return False
    temp = A + A
    if temp.count(B) > 0:
        return True
    else:
        return False

print is_shifted('abcde','cdeab')
print is_shifted('abc', 'acb')
