from collections import Counter
def fun():
    n = int(input())
    nums = list(map(int, input().split()))
    d = Counter(nums)
    if any( a == 1 for a in d.values()):
        return -1
    ans = [0] * n
    a = 0
    for i in range(n-1):
        if nums[i] != nums[i+1]:
            ans[i] = a
            a = i+1
        else:
            ans[i] = i+1
    ans[n-1] = a
    return " ".join(map(str,ans))


if __name__ == "__main__":
    for _ in range(int(input())):
        print(fun())
    
    