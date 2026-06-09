def find_duplicates(lst):
    duplicates = []

    for item in lst:
        if lst.count(item) > 1 and item not in duplicates:
            duplicates.append(item)

    return duplicates

print(find_duplicates([2,5,7,9,3,2,1,2,1]))