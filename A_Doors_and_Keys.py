test = int(input())
for j in range(test):
    string = input()
    s = set()
    for i in range(len(string)):
        if string[i].islower():
            s.add(string[i])
        
        elif string[i].lower() not in s:
            print("NO")
            break
    else:
        print("YES")