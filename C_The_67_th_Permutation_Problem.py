from collections import deque
for _ in range(int(input())):
    n = int(input())
    nums = [num for num in range(1, n*3+1)]
    ans = [0] * (n*3)
    m = deque()
    for i in range(-2, -(n*3), -2):
        m.append(nums[i])
    
    
    a = 0
    for i in range(1, n*3, 3):
        ans[i] = m.popleft()
        ans[i+1] = ans[i] + 1
    
    
    a = 1
    for i in range(0, n*3, 3):
        ans[i]  = a
        a += 1
    print(*ans)


    