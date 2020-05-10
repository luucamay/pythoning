def almost_title(x):
    '''
    x is a string. Make each first letter of each space-separated word uppercase.
    Example: "this is a string" -> "This Is A String"
    '''
    n = len(x)
    w = ''
    ans = ''
    for i in range(n):
        w += x[i]
        if i == (n-1) or x[i] == ' ':
            ans += w[0].upper() + w[1:]
            w = ''
    return ans

def solution(x):
    """
    x is a string using kebab-case or snake_case
    Return the same string using camelCase
    Note: if the first letter is uppercase it should remain like that
    Example: some-random-name => someRandomName
    Example: Some_random_name => SomeRandomName
    """
    n = len(x)
    if n == 0:
        return x
    ans = ''
    i = 0
    while i < n-1:
        if x[i] in ['-', '_']:
            ans += x[i+1].upper()
            i += i
        else:
            ans += x[i]
        i+=1
    if x[n-1] not in ['-', '_']:
        ans += x[n-1]
    return ans
def solution(a, b):
  """
  Difference function, which subtracts one list 
  from another and returns the result.
  It should remove all values from list a, 
  which are present in list b.
  """
  return a
s = input()
print(solution(s))
