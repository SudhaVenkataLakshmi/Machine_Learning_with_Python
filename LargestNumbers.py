def find_largest(lst):
    largest = lst[0]

    for num in lst:
        if num > largest:
            largest = num

    return largest

print(find_largest([11,7,5,3,2,9,12,10,20,15]))