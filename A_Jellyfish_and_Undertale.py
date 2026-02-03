test = int(input())
for _ in range(test):
    max_v, curr_v , tool = map(int, input().split())
    tools = list(map(int, input().split()))
    s  = curr_v
    for a in tools:
        if a>max_v-1:
            s+=max_v-1
        else:
            s+=a
    print(s)
    