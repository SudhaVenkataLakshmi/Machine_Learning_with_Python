print("Enter any String: ")
string = str(input())
print("Enter your digit:")
digit = str(input())
ans = []
for i in range(len(string)):
  if string[i] == digit:
    t = string[:i] + string[(i+1):]
    ans.append(int(t))
    
print("Final Output:")
print(str(max(ans)))