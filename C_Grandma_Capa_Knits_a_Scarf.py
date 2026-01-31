for _ in range(int(input())):
    n = int(input())  
    s = input()
    mini = float('inf')
    
    for l in 'abcdefghijklmnopqrstuvwxyz':
        nws = ""
        c = 0  
        for ch in s:
            if ch == l:   
                c += 1
            else:
                nws += ch
        if nws == nws[::-1]:  
            mini = min(mini, c)
    
    if mini == float('inf'):
        print(-1)
    else:
        print(mini)