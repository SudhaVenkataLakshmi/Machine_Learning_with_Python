a = [
       [-1],
      [2,3],
    [1,-1,-3]
]
ans = 0
for i in range(len(a)-1,0,-1):
    for j in range(len(a[i])-1):
        temp = min(a[i][j],a[i][j+1])
        a[i-1][j] = temp+a[i-1][j]
print(a[0][0])