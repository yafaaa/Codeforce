
for _ in range(int(input())):
    string = input()
    n = len(string)
    s = 0
    for a in string:
        if a == '<':
            s-=1
        elif a == '>':
            s+=1
    if s==0:
        print(-1)
    else:
        print(abs(s))