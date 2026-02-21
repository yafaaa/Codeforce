from collections import Counter
n = int(input())
string = input()
d = Counter(string)
ans = []
if "n" in d:
    ans.extend("1"*d["n"])
if "z" in d:
    ans.extend("0"*d["z"])
if ans[0] == 0:
    print(0)
else:
    print(" ".join(ans))
