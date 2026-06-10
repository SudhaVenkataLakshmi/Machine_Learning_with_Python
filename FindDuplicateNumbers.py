def find_duplicates(lst):
    duplicates = []

    for item in lst:
        if lst.count(item) > 1 and item not in duplicates:
            duplicates.append(item)

    return duplicates

print(find_duplicates([20,40,10,12,20,40,50]))