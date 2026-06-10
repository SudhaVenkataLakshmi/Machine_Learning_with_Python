def lcm(a, b):
    temp_a, temp_b = a, b

    while temp_b:
        temp_a, temp_b = temp_b, temp_a % temp_b

    gcd = temp_a
    return (a * b) // gcd

print(lcm(15,45))