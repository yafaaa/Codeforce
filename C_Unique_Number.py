t = int(input())
for _ in range(t):
    x = int(input())
    if x > 45:
        print(-1)
        continue
    l = []
    s, f = 0, False
    for d in range(9, 0, -1):
        if s + d <= x:
            l.append(d)
            s += d
            if s == x:
                f = True
                break
    if f == False:
        print(-1)
        continue
    
    l.sort()
    num_str = ''.join(map(str, l))
    print(int(num_str))