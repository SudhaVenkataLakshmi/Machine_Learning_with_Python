t = int(input())
ans = []
for i in range(t):
    A,B = input().split()
    a = int(A,2)
    b = int(B,2)
    temp = a + b
    ans.append(temp)
print(max(ans))
print(bin(max(ans)))