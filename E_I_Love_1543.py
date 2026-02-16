
for _ in range(int(input())):
    row, col = map(int, input().split())
    mat = []
    for _ in range(row):
        mat.append(list(input()))
    
    layer = min(row, col)//2
    cnt = 0
    for i in range(layer):
        l = []
        #  l to r
        for c in range(i, col-i):
            l.append(mat[i][c])
        
        # down 
        for r in range(i+1, row-i):
            l.append(mat[r][col-i-1])
        
        # r to l
        for c in range(col-i-2, i-1, -1):
            l.append(mat[row-i-1][c])
        
        # up
        for r in range(row-i-2, i-1, -1):
            l.append(mat[r][i])
        

        l.extend(l[1:3])
        
        cnt += "".join(l).count("1543")
    print(cnt)