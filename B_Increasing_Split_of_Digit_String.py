
for _ in range(int(input())):
    n = int(input())
    nums = list(input())
    # nums = list(map(int, string))
    stack = []
    f = False
    for i, num in enumerate(nums):
        num = nums[i]
        while stack and int("".join(stack)) < int("".join(nums[i:])):
            f = True
            break
        if f:
            print("YES")
            print(2)
            print(int("".join(nums[:i])), int("".join(nums[i:]))) 
            break
        stack.append(num)
    if not f:
        print('NO')