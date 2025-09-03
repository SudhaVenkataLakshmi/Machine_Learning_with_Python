def sum_list(lst):
    return sum(lst)
def sum_list_manual(lst):
    total = 0
    for num in lst:
        total += num
    return total
lst = [5,8,3,4,2,7]
print("Sum: ",sum_list(lst))