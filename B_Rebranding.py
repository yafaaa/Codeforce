lenght, query = map(int, input().split())
string = input()
sub_d =[i for i in range(26)]
main_d = [chr(ord('a')+i) for i in range(26)]
res = []
for _ in range(query):
    x, y = input().split()
    idxx = sub_d[ord(x)-97]
    idxy = sub_d[ord(y)-97]
    main_d[idxx], main_d[idxy] = main_d[idxy], main_d[idxx]
    sub_d[ord(x)-97], sub_d[ord(y)-97] = sub_d[ord(y)-97], sub_d[ord(x)-97]
for s in string:
    res.append(main_d[ord(s)-97])
print("".join(res))