lenght, query = map(int, input().split())
string = input()
trace =[i for i in range(26)]
actual = [chr(ord('a')+i) for i in range(26)]
res = []
for _ in range(query):
    x, y = input().split()
    idxx = trace[ord(x)-97]
    idxy = trace[ord(y)-97]
    actual[idxx], actual[idxy] = actual[idxy], actual[idxx]
    idxx, idxy = idxy, idxx
for s in string:
    res.append(actual[ord(s)-97])
print("".join(res))