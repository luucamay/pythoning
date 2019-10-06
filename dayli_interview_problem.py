def logest_consecutive(numbers):
    longest_len = 0
    numbers.sort()
    aux_counter = 1
    i = 0
    for number in numbers:
        i += 1
        if i < len(numbers):
            if (number+1) == numbers[i]:
                aux_counter += 1
            else:
                if longest_len < aux_counter:
                    longest_len = aux_counter
                aux_counter = 1
    return longest_len

# Test
print (logest_consecutive([8,10,13,14,1,100,7,6,9,5]))
print (logest_consecutive([100,4,200,1,3,2]))
