n = "235432"
digit = "3"
ans = []
for p in range(len(n)):
    if n[p] == digit:
        temp = n[0:p] + n[p+1: ]
        ans.append(temp)
print(str(max(ans)))