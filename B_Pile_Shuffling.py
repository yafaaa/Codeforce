t = int(input())
for i in range(t):
    # if i < 3 or i >= 9:
        n = int(input())
        s = 0
        a = b = c = d = 0
        for _ in range(n):
            a,b,c,d =map(int,input().split())
            if a>c:
                s += (a-c)

            if b>d:
                s += min(a,c)+b-d 
                

        print(s)
    

