
for _ in range(1):
    n = int(input())
    string = input()
    if len(string) == 1:
        print("Yes")
        continue

    for s in set(string):
        if string.count(s) >= 2:
            print('Yes')
            break
    else:
        print('No')

