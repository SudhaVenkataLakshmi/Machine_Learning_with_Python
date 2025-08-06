# a = int(input("Enter First Number: "))
# b = int(input("Enter Second Number: "))
# c = a ^ b
# print("Bitwise XOR Operation of ", a ,"and", b ,"=", c)


def findSum(n,k):
    val = (k // (n-1) * n);
    rem = k % (n-1);
    if(rem == 0):
        val = val + rem;
        sum = (val * (val + 1)) // 2;
        x = k // (n-1);
        sum
