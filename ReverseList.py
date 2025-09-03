def reverse_list(lst):
    left = 0
    right = len(lst) - 1
    while left < right:
        lst[left], lst[right] = lst[right], lst[left]
        left += 1
        right -= 1
lst = [1,2,3,4,5]
reverse_list(lst)
print("Reversed List: ",lst)