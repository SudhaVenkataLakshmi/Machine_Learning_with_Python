arr = [3,5,6,7,2,4,5,2,5,6,8]
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