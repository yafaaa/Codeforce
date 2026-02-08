from collections import Counter
for _ in range(int(input())):
    s = input()
    t = input()
    p = input()
    dict_p = Counter(p)
    idx_s = 0
    len_s=len(s)
    f = True
    for ch in t:
        if idx_s<len_s and ch == s[idx_s]:
            idx_s+=1
        elif ch not in dict_p:
            f = False
            break
        else:
            dict_p[ch]-=1
            if dict_p[ch]==0:
                del dict_p[ch]
    if f and idx_s==len_s:
        print("YES")
    else:
        print("NO")

