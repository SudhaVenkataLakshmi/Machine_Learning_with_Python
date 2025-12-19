n = "1125"
digit = "1"
ans = []
for p in range(len(n)):
    if n[p] == digit:
        temp = n[0:p] + n[p+1: ]
        ans.append(temp)
print(str(max(ans)))