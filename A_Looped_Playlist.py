n , s = map(int, input().split())
nums = list(map(int, input().split()))
a = 0
curr_s = 0
min_len = n
idx, lens = 0, 0
t = n*(s//sum(nums))
s %= sum(nums)
for b in range(2*n):
    curr_s += nums[b%n]
    if curr_s < s:
        continue
    while curr_s >= s:
        if b-a+1 < min_len:
            idx = a
            min_len = b-a+1
        curr_s -= nums[a%n]
        a += 1
print((idx%n)+1, t+min_len)
    



