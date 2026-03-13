for _ in range(int(input())):
    n = int(input())
    string = input()
    ans = []
    prefix = 0
    f = False
    for i in range(n):
        if int(string[i]) % 2:
            ans.append(string[i])
            prefix += int(string[i])

            if not prefix % 2:
                print("".join(ans))
                f = True
                break
    if not f:
        print(-1)