for _ in range(int(input())):
    n = map(int, input())
    s = input()
    mini = float('inf')
    for c in 'abcdefghijklmnopqrstuvwxyz':
        nws = ""
        c = 0
        for char in s:
            if char == c:
                c += 1
            else:
                nws += char
        if nws == nws[::-1]:
            mini = min(mini, c)
    
    if mini == float('inf'):
        print (-1)
    else:
        print (mini)