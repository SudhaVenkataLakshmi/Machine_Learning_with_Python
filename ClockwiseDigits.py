arr = [7,8,5,5,9,2,2,0,1,6]
res = arr[0:3][::-1]
# print(res)
res = res + arr[3:][::-1]
print(res)
ans = 0
final = 0
for i in res:
    ans ^= i
    final = final + ans
print(final)