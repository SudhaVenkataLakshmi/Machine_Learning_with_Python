A = [[3,4],[1,2]]
B = [[7,8],[5,6]]

result = []

for i in range(len(A)):
    row = []
    for j in range(len(A[0])):
        row.append(A[i][j] + B[i][j])
    result.append(row)

print(result)