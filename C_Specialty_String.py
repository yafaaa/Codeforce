
for _ in range(int(input())):
    n = int(input())
    string = list(input())
    if not string:
        print("NO")
        continue
    stack = []
    for i in range(len(string)):
        if string[i] != "*":
            if stack and stack[-1] == string[i]:
                stack.pop()
            else:
                stack.append(string[i])
                
    if not stack:
        print("YES")
    else:
        print("NO")

