def deletion_distance(str1, str2):
    s1 = len(str1)
    s2 = len(str2)
    if s1 == 0:
        return s2
    if s2 == 0:
        return s1
    output = 0
    while s1 > 0 and s2 > 0:
        if str1[0] != str2[0]:
            if s1 > s2:
                str1 = str1[1:]
            else:
                str2 = str2[1:]
            output += 1
        else:
            str1 = str1[1:]
            str2 = str2[1:]
        s1 = len(str1)
        s2 = len(str2)
    output += max(s1, s2)
    return output

# Test cases
print deletion_distance("", "")
print deletion_distance("", "hit")
print deletion_distance("neat", "")
print deletion_distance("heat", "hit")
print deletion_distance("hot", "not")
print deletion_distance("some", "thing")
print deletion_distance("abc", "adbc")
print deletion_distance("awesome", "awesome")
print deletion_distance("ab", "ba")
