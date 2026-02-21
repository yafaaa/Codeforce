


    
n, k = map(int, input().split())

road = input().strip()

co = 0
f = False
for ch in road:
    if ch == '#':
        co += 1
        
        if co >= k:
            print("NO")
            f = True
            break
    else:
        
        co = 0
if not f:    
    print("YES")

