N, X = map(int, input().split())
A = list(map(int, input().split()))

flag = False
for i in range(N):
    if A[i] == X:
        flag = True
        break

if flag:
    print("Yes")
else:
    print("No")
