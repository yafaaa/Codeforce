for _ in range(int(input())):
    shelv, n = map(int, input().split())
    
    boxes = []
    for _ in range(n):
        x, y = map(int, input().split())
        boxes.append((x, y))
        
    boxes.sort()
    

    l = []
    if n > 0:
        current_brand_sum = boxes[0][1]
        for i in range(1, n):
            if boxes[i][0] == boxes[i-1][0]:
                current_brand_sum += boxes[i][1]
            else:
                l.append(current_brand_sum)
                current_brand_sum = boxes[i][1]
        l.append(current_brand_sum)
    
    l.sort(reverse=True)
    
    res = 0
    for i in range(shelv):
        if i < len(l):
            res += l[i]
            
    print(res)