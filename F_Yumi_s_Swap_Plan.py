n = int(input())
string = input()
k = string.count("H") #k is count of h
string = string + string
cnt_t = string[:k].count("T")
mn = cnt_t
for b in range(k, 2*n):
    a = b-k+1
    if string[b] == "T":
        cnt_t += 1
    if string[a-1] == "T":
        cnt_t -= 1
    mn = min(cnt_t,mn)
print(mn)
    