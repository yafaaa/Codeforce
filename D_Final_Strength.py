import bisect
def fun():
    n = int(input())
    nums = list(map(int, input().split()))

    def merge(l,r):
        if l == r:
            return [[nums[l], l]]
        mid = (l+r)//2
        left_arr = merge(l,mid)
        right_arr = merge(mid+1, r)
        
        for num, i in left_arr:
            idx = bisect.bisect_left(right_arr, [num, float('-inf')])
            nums[i] += idx
        
        return sorted(left_arr + right_arr)
    
    ans = merge(0, len(nums)-1)
    
    
    for a, b in ans:
        print(a, end= " ")
    
    print()

    
for _ in range(int(input())):
    fun()
