for _ in range(int(input())):
    n, w = list(map(int, input().split()))
    t = n//w
    print(t*(w-1) + n%w)
    
    
