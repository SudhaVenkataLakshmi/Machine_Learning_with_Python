for num in range(1,1001):
    order = len(str(num))
    s = sum(int(d)**order for d in str(num))
    if s == num:
        print(num, end= " ")