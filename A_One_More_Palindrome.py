for _ in range(int(input())):
    s = input()
    n = len(s)
    if len(set(s[:((n)//2)])) > 1:
        print("YES")
    else:
        print("NO")