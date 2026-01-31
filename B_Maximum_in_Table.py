t = int(input())
n= [[1] * t for _ in range(t)]
for i in range(1, t):
    for j in range(1,t):
        n[i][j] = n[i][j-1] + n [i-1][j]
print(max(n[t-1]))
