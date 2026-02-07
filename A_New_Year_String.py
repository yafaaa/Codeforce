test = int(input())
for _ in range(test):
    length = int(input())
    string = input()
    f = True
    p = False
    if "2026" in string:
        print("0")
    elif "2025" in string:
        print("1")
    else:
        print("0")
