n, m = map(int, input().split())
matrix = []

for _ in range(n):
    matrix.append(list(input()))

direction = [(1,0), (-1,0), (0,-1), (0, 1)]

def inbound(r,c):
    return 0 <= r < n and 0 <= c < m

def dfs(r,c, ch, pr, pc):
    
    matrix[r][c] = 1
    for dr, dc in direction:
        nw_r = dr + r
        nw_c = dc + c

        if not inbound(nw_r, nw_c) or matrix[nw_r][nw_c] != ch or matrix[nw_r][nw_c] == 2:
            continue
        
        
    matrix[r][c] = 2
