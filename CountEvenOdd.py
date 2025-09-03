def count_even_odd(lst):
    even_count = 0
    odd_count = 0
    for num in lst:
        if num % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    return even_count, odd_count
lst = [3,6,8,2,5,6,9,4]
even, odd = count_even_odd(lst)
print("Even count: ", even, "Odd count: ", odd)