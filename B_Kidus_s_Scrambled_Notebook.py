test = int(input())
for _ in range(test):
    string = input()
    n = len(string)
    for i in range(n-1,0,-1):
        str_a = string[:i]
        str_b = string[i:]
        if str_b[0] =="0":
            continue
        if int(str_a)<int(str_b):
            print(str_a, str_b)
            break
    else:
        print(-1)

        