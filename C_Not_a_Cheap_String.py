from collections import Counter
for i in range(int(input())):
    string = input()
    k = int(input())
    n = len(string)
    d = Counter(string)
    d_sorted = sorted(d.items(), key = lambda x: x[0], reverse=True)
    curr_s = 0
    for key, v in d_sorted:
        curr_s += ((ord(key) - 96) * v)

    for key, _ in d_sorted:
        val = ord(key) - 96
        if curr_s <= k:
            break
        while d[key] and curr_s > k and curr_s >= val:
            curr_s -= val
            d[key] -= 1
        
    res = []

    for ch in string:
        if d[ch]:
            res.append(ch)
            d[ch] -= 1
    print("".join(res))


    