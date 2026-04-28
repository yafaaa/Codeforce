
def solve():
    n = int(input())
    nums = list(map(int, input().split()))
    cnt = 0

    def fun(nums):
        nonlocal cnt
        mid = len(nums)//2
        if len(nums)<2:
            return nums
        left = fun(nums[:mid])
        right = fun(nums[mid:])

        if left[0] > right[0]:
            cnt += 1
            return right + left
        
        return left + right

    rtrn = fun(nums)
    

    if rtrn == [ i for i in range(1, n+1)]:
        return cnt
    else:
        return -1


for _ in range(int(input())):
    print(solve())



