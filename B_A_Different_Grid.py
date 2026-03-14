def fun(n, m):
    mat = []
    for i in range(n):
        mat.append(list(map(int, input().split())))

    for i in range(n):
        for j in range(m):
            if (mat[i][j]+1) > m*n:
                ans = (mat[i][j]+1) % m*n + 1

                ans = ((mat[i][j]+1) % (m*n+1)) + 1
            else: 
                ans = ((mat[i][j]+1) % (m*n+1)) 
            if ans == mat[i][j]:
                mat = [[-1]]
                return mat
            mat[i][j] = ans
    return mat
if __name__ == "__main__":
    for _ in range(int(input())):
        n, m = map(int, input().split())
        res = fun(n, m)
        for i in range(len(res)):
            print(*res[i])