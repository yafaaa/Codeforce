
for _ in range(int(input())):
    n, m = map(int, input().split())
    string = input()
    w = input()
    
    s = [ ord(ch) for ch in string]
    w = [ ord(ch) for ch in w]
    
    a = 0
    curr = 0
    
    target = sum(w)

    for b in range(n):
        curr += s[b]
        
        if b-a+1 > m or curr > target:
            curr -= s[a]
            a += 1
        if b-a+1 == m and curr == target:
            print("YES")
            break
    else:
        print("NO")


    
    
