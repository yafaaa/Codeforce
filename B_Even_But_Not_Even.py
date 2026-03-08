for _ in range(int(input())):
    n = int(input())
    s = input()
    ans = ""
    for char in s:
        if int(char) % 2 != 0:
            ans += char
        
        if len(ans) == 2:
            break
            
    if len(ans) == 2:
        print(ans)
    else:
        print(-1)