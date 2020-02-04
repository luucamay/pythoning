def abbreviation(word):
    new_word = word
    size = len(word)
    if size > 10:
        new_word = word[0] + str(size-2) + word[size-1]
    return new_word
n = int(input())
for line in range(n):
    word = input()
    print(abbreviation(word))
