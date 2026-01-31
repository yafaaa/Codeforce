s = input()
h = "hello"
x = 0
f = False
for a in h:
    
    while x<len(s) and a!=s[x]:
        x+=1
    if x>len(s)-1:
            print("NO")
            break  
    x+=1
else:
    print("YES")

    

    



        
        