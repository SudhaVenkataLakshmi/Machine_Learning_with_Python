t = int(input())
ans = []
for i in range(t):
    m,n = input().split()
    M = int(m, 2)
    N = int(n, 2)
    temp = M + N
    ans.append(temp)
# print(ans)
# print(max(ans))
final = bin(max(ans))
print("Final Output is: ")
print(final[2:])
