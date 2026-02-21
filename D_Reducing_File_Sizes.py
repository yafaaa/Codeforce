def fun():
    n, k = list(map(int, input().split()))
    nums = []
    s = 0
    for _ in range(n):
        x, y = list(map(int, input().split()))
        s += x
        nums.append([x,y])
    cnt = 0
    if s <= k:
        return cnt
    nums.sort(key = lambda x: -(abs(x[0]-x[1])))

    for i in range(n):
        s -= nums[i][0]
        s += nums[i][1]
        cnt += 1
        if s <=k:
            return cnt
    return -1

if __name__ == "__main__":
    print(fun())
