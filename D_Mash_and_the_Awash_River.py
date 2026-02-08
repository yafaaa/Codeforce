
for _ in range(int(input())):
    string = input()
    n = len(string)
    if "><" in string or "*<" in string or ">*" in string or "**" in string:
        print(-1)
        continue
    if string[0]=="*" or string[-1]=="*":
        print(n)
        continue
    m = 1
    prev = string[0]
    for i in range(1,n):
        ch = string[i]
        if ch != prev:
            if ch == "*":
                m = max(n-(i+1), i)+1
            else:
                m = max(n-(i), i)
            break
        m+=1
    print(m)
        


