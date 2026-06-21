def find_duplicates(lst):
    duplicates = []

    for item in lst:
        if lst.count(item) > 1 and item not in duplicates:
            duplicates.append(item)

    return duplicates

print(find_duplicates([2,4,7,9,12,1,11,3,7,7,2]))