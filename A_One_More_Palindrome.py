for _ in range(int(input())):
    s = input()
    first = set(s[:len(s)//2])
    if len(first) > 1:
        print("YES")
    else:
        print("NO")