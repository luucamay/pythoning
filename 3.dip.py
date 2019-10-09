def is_shifted(A, B):
    if len(A) == len(B) and len(A) > 0:
        indexB = B.find(A[0])
        if indexB > -1:
            for indexA in range(len(A)):
                if A[indexA] == B[indexB]:
                        indexB += 1
                        indexB = indexB % len(B)
                else:
                    return False
            return True
    return False

print is_shifted('abcde','cdeab')
