
for _ in range(int(input())):
    n = int(input())
    mat = []
    d = dict()
    for row in range(n):
        mat.append(list(map(int,input())))
    
    cnt = 0
    
    
    for r in range(n//2):
        for c in range((n+1)//2):

            p1 = mat[r][c]
            p2 = mat[c][n-1-r]
            p3 = mat[n-1-r][n-1-c]
            p4 = mat[n-1-c][r]

            total = p1 + p2 + p3 + p4
            cnt += min(total, 4-total)

    print(cnt)
            
    

    