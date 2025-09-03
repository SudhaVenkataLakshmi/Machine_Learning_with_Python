def find_largest(lst):
    if not lst:
        return None
    return max(lst)
def find_largest_manual(lst):
    if not lst:
        return None
    largest = lst[0]
    for num in lst:
        if num > largest:
            largest = num
    return largest
lst = [3,6,1,2,7,9,12,23,5]
print("Largest Element: ", find_largest(lst))